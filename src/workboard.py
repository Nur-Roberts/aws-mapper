from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, VPC, PublicSubnet, PrivateSubnet

with Diagram("Grouped Workers", show=True, direction="TB"):
    with Cluster("vpcID:29183"):
        VPC("vpcID:29183")
        with Cluster("AZ1"):
            with Cluster("Subnet1"):
                PublicSubnet("Pub-sub-1")
            with Cluster("Subnet2"):
                PrivateSubnet("Priv-sub-1")
        with Cluster("AZ2"):
            with Cluster("Subnet3"):
                PublicSubnet("Pub-sub-2")
            with Cluster("Subnet4"):
                PrivateSubnet("Priv-sub-3")