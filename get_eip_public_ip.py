import boto3
from typing import List
import click

ecs = boto3.client('ecs')
ec2 = boto3.client('ec2')


def list_tasks(cluster_id: str) -> dict:
    return ecs.list_tasks(cluster=cluster_id).get('taskArns')


def describe_tasks(cluster_id: str, task_ids: List[str]) -> dict:
    return ecs.describe_tasks(cluster=cluster_id, tasks=task_ids)


def describe_network_interface(enis: List[str]) -> dict:
    return ec2.describe_network_interfaces(NetworkInterfaceIds=enis)


@click.command()
@click.option('--cluster-id', help='The ECS cluster id')
def cli(cluster_id: str):
    """Get public EIP addresses for the containers for a certain ECS cluster"""
    try:
        list_of_eni: List[str] = []
        tasks: List[str] = list_tasks(cluster_id)
        tasks = describe_tasks(cluster_id, tasks).get('tasks')
        for task in tasks:
            attachments = task.get('attachments')
            for attachment in attachments:
                details = attachment.get('details')
                for detail in details:
                    if detail.get('name') == 'networkInterfaceId' and detail.get('value').startswith('eni'):
                        list_of_eni.append(detail.get('value'))

        network_interface_descriptions = describe_network_interface(list_of_eni)
        for interface in network_interface_descriptions.get('NetworkInterfaces'):
            public_dns = interface.get('Association').get('PublicDnsName')
            public_ip = interface.get('Association').get('PublicIp')
            print(f"- public_dns: {public_dns}")
            print(f"- public_ip: {public_ip}")


    except Exception as err:
        print(err)


if __name__ == '__main__':
    cli()
