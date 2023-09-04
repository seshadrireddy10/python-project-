# Use this below method to create azure service principal 

The quickest way and easiest way to create this Service Principal is to use Azure CLI and issue the command: 

```sh
az ad sp create-for-rbac \
    --name "myAzureServiceGitHubConnection" \
    --role contributor \
    --scopes /subscriptions/e94972e2-c0eb-497c-8f74-f98b46621f80/resourceGroups/sai-arch \
    --sdk-auth 
```

# Execute below powershell commands in Azure to collect Service Principal information 

To store the information inside a GitHub Actions secret, it needs to be stored within a JSON format.  We can run this PowerShell subscription to collect all the information you will need for GitHub and in the form that GitHub needs.


```sh
$ServicePrincipalName = "MyGithubActionsConnection"
$AzSubscriptionName = "production"

Connect-AzureAD

$Subscription = (Get-AzSubscription -SubscriptionName $AzSubscriptionName)
$ServicePrincipal = Get-AzADServicePrincipal -DisplayName $ServicePrincipalName
$AzureADApplication = Get-AzureADApplication -SearchString $ServicePrincipalName

$OutputObject = [PSCustomObject]@{
    clientId = $ServicePrincipal.AppId
    clientSecret = (New-AzureADApplicationPasswordCredential -ObjectId $AzureADApplication.ObjectId).Value
    subscriptionId = $Subscription.Id
    tenantId = $Subscription.TenantId
}

$OutputObject | ConvertTo-Json 
```


# Expected output of the above commands and copy as the below mentioned json format to AZURE_CREDENTIALS

Take a copy of the output from the PowerShell query.  This will be stored inside a GitHub Secret for use within your workflows.
Within the repository where your workflow is, click on Settings > Secrets > Actions and then click on new repository secret.

```sh
{
  "clientId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "clientSecret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "subscriptionId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}```