Imagine you now have these three files:

api_documentation.json
physical_data_model.json
reference_data.json

You want to write some code that contains a parser that is able to load all of these 3 files and output a final merged json file called data_artifacts.json

And I would like to allow some for of monitoring or versioning history on another files as well that would be able to track any changes on these data models as well. Not sure what would be the best way to organize this though. 

Please notice that we are working on a python framework and all files are in the local directory. Please note that the code written must contain some basic logging capabilities


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
      "db_customer_addresses": {
        "description": "Stores customer delivery addresses",
        "columns": {
          "address_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["PRIMARY KEY"], "description": "Unique identifier for address"},
          "customer_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["FOREIGN KEY"], "description": "Reference to customers table"},
          "address_line1": {"type": "VARCHAR(100)", "is_nullable": false},
          "address_line2": {"type": "VARCHAR(100)", "is_nullable": true},
          "city": {"type": "VARCHAR(50)", "is_nullable": false},
          "postal_code": {"type": "VARCHAR(10)", "is_nullable": false},
          "country": {"type": "VARCHAR(2)", "is_nullable": false, "description": "ISO country code"},
          "is_default": {"type": "BOOLEAN", "is_nullable": false, "default": false}
        }
      },
      "db_orders": {
        "description": "Stores order information",
        "columns": {
          "order_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["PRIMARY KEY"], "description": "Unique identifier for order"},
          "customer_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["FOREIGN KEY"], "description": "Reference to customers table"},
          "delivery_address_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["FOREIGN KEY"], "description": "Reference to customer_addresses table"},
          "order_status": {"type": "VARCHAR(20)", "is_nullable": false, "description": "Current order status"},
          "total_amount": {"type": "DECIMAL(10,2)", "is_nullable": false},
          "payment_method": {"type": "VARCHAR(20)", "is_nullable": false, "description": "Payment method used for the order"},
          "created_at": {"type": "TIMESTAMP", "is_nullable": false},
          "updated_at": {"type": "TIMESTAMP", "is_nullable": false}
        }
      },
      "db_shipments": {
        "description": "Stores shipment tracking information",
        "columns": {
          "shipment_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["PRIMARY KEY"]},
          "order_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["FOREIGN KEY"]},
          "lsp_provider": {"type": "VARCHAR(20)", "is_nullable": false},
          "tracking_number": {"type": "VARCHAR(100)", "is_nullable": true},
          "shipment_status": {"type": "VARCHAR(20)", "is_nullable": false},
          "shipping_method": {"type": "VARCHAR(20)", "is_nullable": false, "description": "Shipping method used for the shipment"},
          "estimated_delivery": {"type": "TIMESTAMP", "is_nullable": true},
          "created_at": {"type": "TIMESTAMP", "is_nullable": false},
          "updated_at": {"type": "TIMESTAMP", "is_nullable": false}
        }
      },
      "db_products": {
        "description": "Stores product information",
        "columns": {
          "product_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["PRIMARY KEY"], "description": "Unique identifier for product"},
          "product_name": {"type": "VARCHAR(255)", "is_nullable": false, "description": "Name of the product"},
          "price": {"type": "DECIMAL(10,2)", "is_nullable": false, "description": "Price of the product"},
          "product_category": {"type": "VARCHAR(50)", "is_nullable": false, "description": "Category of the product"},
          "created_at": {"type": "TIMESTAMP", "is_nullable": false, "description": "Record creation timestamp"}
        }
      },
      "db_order_items": {
        "description": "Stores order items information",
        "columns": {
          "order_item_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["PRIMARY KEY"], "description": "Unique identifier for order item"},
          "order_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["FOREIGN KEY"], "description": "Reference to orders table"},
          "product_id": {"type": "BIGINT", "is_nullable": false, "constraints": ["FOREIGN KEY"], "description": "Reference to products table"},
          "quantity": {"type": "INTEGER", "is_nullable": false, "description": "Quantity of the product ordered"},
          "price": {"type": "DECIMAL(10,2)", "is_nullable": false, "description": "Price of the product at the time of order"}
        }
      }
    }
  }
}
