## Un-used AWS Resources

To identify Unused resources in AWS , Just import these package and call the `unused_res` with the following parameters

    ```python
    unused_res("12", "xyz@gmail.com",
               "zyx@gmail.com", "SAP", "sbx")
    ```           

# Days 
    From How long these resources has not been used. For example , If we provide days as `14`, Start date will be today date -14 , end date will be today's date.

# Sender
    We have used SES to send the formatted mail(html), so it is the Mail Id from where it need to send.

# Receiver
    Receiver Mail Id

# App
    For sending the subject in mail , we need these application information. Ex: SAP, ACE etc..,

# Env
    Against which environment is running these code. Ex: SBX, DEV,INT etc..,

# As of now , the following resources can be identified as unused(`Based on CPU Utilization , Invocation/request count etc..,`) if they didn't used for the specified number of days.

`AWS::EC2::Volume`
`AWS::EC2::EIP` 
`AWS::Elasticsearch::Domain`
`AWS::ECS::Service`
`AWS::EC2::SecurityGroup` 
`AWS::EC2::Instance`
`AWS::EC2::NatGateway`
`AWS::ElasticLoadBalancingV2::LoadBalancer` 
`AWS::ACM::Certificate`
`AWS::RDS::DBCluster`
`AWS::S3::Bucket` 
`AWS::DynamoDB::Table`
`AWS::CodeBuild::Project`
`AWS::Lambda::Function` 
`AWS::ApiGateway::RestApi`
`AWS::ApiGatewayV2::Api`
`AWS::CodePipeline::Pipeline` 
`AWS::SQS::Queue`
`AWS::SNS::Topic`
`AWS::SecretsManager::Secret` 
`AWS::Logs::LogGroup`

Many more will be added in the future

# Note:

To Package these file we need `WSL` or `Linux System/container` . 

Few  issues which I faced during packaging : https://github.com/numpy/numpy/issues/13465