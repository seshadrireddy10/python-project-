# Use this below method to create azure service principal 

# Commad to be executed form Azure 
az ad sp create-for-rbac \
    --name "myAzureServiceGitHubConnection" \
    --role contributor \
    --scopes /subscriptions/e94972e2-c0eb-497c-8f74-f98b46621f80/resourceGroups/sai-arch \
    --sdk-auth

# Execute below powershell commands in Azure to generate the output for AZURE_CREDENTIALS   

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


# Expected output of the above commands and copy as the below mentioned json format to AZURE_CREDENTIALS

{
  "clientId": "7b367077-d2ed-41b4-99f1-8b0f5b0e9ca7",
  "clientSecret": "usNonfiGXJXvwlC9FyUzcAzn8OIgHe2JLCuaiEemH+Y=",
  "subscriptionId": "e94972e2-c0eb-497c-8f74-f98b46621f80",
  "tenantId": "9b4947ce-08e8-47b9-9c2d-c39b90bfaa7e"
}