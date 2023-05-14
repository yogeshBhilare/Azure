resource "azurerm_mssql_server" "primary" {
  name                         = var.primary_database
  resource_group_name          = var.resource_group
  location                     = var.location
  version                      = "12.0"
  administrator_login          = var.primary_database_admin
  administrator_login_password = var.primary_database_password
}

resource "azurerm_mssql_database" "db" {
  name      = "db"
  server_id = azurerm_mssql_server.primary.id
  collation = "SQL_Latin1_General_CP1_CI_AS"
  tags = {
    tier = "database"
  }
}
