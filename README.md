# aws_unused_res

Repo for packaging the python code - to find the unused resources in AWS

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


# In EC2 -Linux Instance

If you are using EC2 linux instance to package these code , then use the below commands to install the PIP

`curl -O https://bootstrap.pypa.io/get-pip.py`

`python3 get-pip.py`

`sudo yum -y install python-pip`

# Commands to install the package and upload it in [PyPI](https://pypi.org/project/):

`python -m pip install --upgrade pip setuptools wheel`
`python -m pip install tqdm`
`python -m pip install --user --upgrade twine`

From your Package code path (setup files), run the below commands

`python setup.py sdist bdist_wheel`
`python -m twine upload --repository pypi dist/*`

Ref: (https://packaging.python.org/tutorials/packaging-projects/)

# Contributing

# Issues

Kindly create issues [here](https://github.com/karthickcse05/aws_unused_res/issues)