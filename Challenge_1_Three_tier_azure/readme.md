
**Problem statment**
A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these
resources on a cloud environment (Azure/AWS/GCP). Please remember we will not be judged
on the outcome but more focusing on the approach, style and reproducibility.


**Solution Overview**
T
This terraform code  deploys a 3 Tier Red Hat Solution on Azure.The Solution includes Web tier Servers, Application tier Servers Tier Servers running Linux server and user Azure MSSQL database. 

![alt text](https://github.com/yogeshBhilare/Azure/blob/main/image.jpg?raw=true)

**Template Solution Architecture**

This template will deploy:

resource_group : create resource group for all resources azure-stack
Network        : created private network vnet01 , with 3 subnet web-subnet,app-subnet,db-subnet
Security Group : 3 security groups web-nsg , app-nsg and db-nsg
Database       : MSSQL server and database
Compute        :  3 Avaibility sets to get fault tollarence - web_availabilty_set,app_availabilty_set,db_availabilty_set
                  2 Network interfaces - web-net-interface,app-net-interface,db-net-interface
                  2 Azure vms web-vm , app-vm
                  
 
**Terraform variables template (var.tf) :**
    variable "rsgname" {}
    variable "location" {}
    variable "vnet_name" {}
    variable "vnetcidr" {}
    variable "websubnetcidr" {}
    variable "appsubnetcidr" {}
    variable "dbsubnetcidr" {}
    variable "web_host_name" {}
    variable "web_username" {}
    variable "web_os_password" {}
    variable "app_host_name" {}
    variable "app_username" {}
    variable "app_os_password" {}
    variable "primary_database" {}
    variable "primary_database_admin" {}
    variable "primary_database_password" {}
    variable "primary_database_version" {}

**Sample variable values (terraform.tfvars):**
    rsgname                   = "azure-stack"
    location                  = "Central India"
    vnet_name                 = "vnet01"

    vnetcidr                  = "192.168.0.0/16"
    websubnetcidr             = "192.168.1.0/24"
    appsubnetcidr             = "192.168.2.0/24"
    dbsubnetcidr              = "192.168.3.0/24"

    web_host_name             = "webserver"
    web_username              = "web_user"
    web_os_password           = "@Webuser1"

    app_host_name             = "appserver"
    app_username              = "app_user"
    app_os_password           = "@Appuser1"

    primary_database          = "sql-primary-database-yogee"
    primary_database_admin    = "sqladmin"
    primary_database_password = "pa$$w0rd"
    primary_database_version  = "12.0"
