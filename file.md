    "physical_data_model": {
        "tables": {
            "db_customers": {
                "description": "Stores customer information and delivery addresses",
                "columns": {
                    "customer_id": {
                        "type": "BIGINT",
                        "is_nullable": false,
                        "constraints": [
                            "PRIMARY KEY"
                        ],
                        "description": "Unique identifier for customer"
                    },
                    "email": {
                        "type": "VARCHAR(255)",
                        "is_nullable": false,
                        "description": "Customer email address"
                    },
                    "created_at": {
                        "type": "TIMESTAMP",
                        "is_nullable": false
                    },
                    "updated_at": {
                        "type": "TIMESTAMP",
                        "is_nullable": false
                    }
                }
            },

{
  "physical_data_model": {
    "tables": {
      "db_customers": {
        "description": "Stores customer information and delivery addresses",
        "columns": {
          "customer_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["PRIMARY KEY"], "description": "Unique identifier for customer"},
          "email": {"type": "VARCHAR(255)", "is_nullable": false, "description": "Customer email address"},
          "created_at": {"type": "TIMESTAMP", "is_nullable": false},
          "updated_at": {"type": "TIMESTAMP", "is_nullable": false}
        }
      },
