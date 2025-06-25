import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')

  
    stop_instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Stop']}]
    )
    stop_ids = [instance.id for instance in stop_instances if instance.state['Name'] != 'stopped']
    if stop_ids:
        ec2.instances.filter(InstanceIds=stop_ids).stop()
        print(f"Stopped instances: {stop_ids}")
    else:
        print("No Auto-Stop instances need stopping.")

 
    start_instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Start']}]
    )
    start_ids = [instance.id for instance in start_instances if instance.state['Name'] != 'running']
    if start_ids:
        ec2.instances.filter(InstanceIds=start_ids).start()
        print(f"Started instances: {start_ids}")
    else:
        print("No Auto-Start instances need starting.")
