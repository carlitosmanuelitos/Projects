{
  "metadata": {
    "version": "1.0",
    "generated_date": "2025-01-13",
    "environment": "e-commerce",
    "description": "Current state of e-commerce platform before same-day delivery feature"
  },
  "physical_data_model": {
    "tables": [
      {
        "name": "customers",
        "description": "Stores customer information and delivery addresses",
        "columns": [
          {
            "name": "customer_id",
            "type": "BIGINT",
            "is_nullable": false,
            "constraints": ["PRIMARY KEY"],
            "description": "Unique identifier for customer"
          },
          {
            "name": "email",
            "type": "VARCHAR(255)",
            "is_nullable": false,
            "description": "Customer email address"
          },
          {
            "name": "phone",
            "type": "VARCHAR(20)",
            "is_nullable": true,
            "description": "Customer contact number"
          },
          {
            "name": "created_at",
            "type": "TIMESTAMP",
            "is_nullable": false,
            "description": "Record creation timestamp"
          }
        ],
        "indexes": [
          {
            "name": "idx_customers_email",
            "columns": ["email"],
            "unique": true
          }
        ]
      },
      {
        "name": "customer_addresses",
        "description": "Stores customer delivery addresses",
        "columns": [
          {
            "name": "address_id",
            "type": "BIGINT",
            "is_nullable": false,
            "constraints": ["PRIMARY KEY"],
            "description": "Unique identifier for address"
          },
          {
            "name": "customer_id",
            "type": "BIGINT",
            "is_nullable": false,
            "constraints": ["FOREIGN KEY"],
            "description": "Reference to customers table"
          },
          {
            "name": "address_line1",
            "type": "VARCHAR(100)",
            "is_nullable": false
          },
          {
            "name": "address_line2",
            "type": "VARCHAR(100)",
            "is_nullable": true
          },
          {
            "name": "city",
            "type": "VARCHAR(50)",
            "is_nullable": false
          },
          {
            "name": "postal_code",
            "type": "VARCHAR(10)",
            "is_nullable": false
          },
          {
            "name": "country",
            "type": "VARCHAR(2)",
            "is_nullable": false,
            "description": "ISO country code"
          },
          {
            "name": "is_default",
            "type": "BOOLEAN",
            "is_nullable": false,
            "default": false
          }
        ],
        "indexes": [
          {
            "name": "idx_addresses_customer",
            "columns": ["customer_id"]
          },
          {
            "name": "idx_addresses_postal",
            "columns": ["postal_code", "country"]
          }
        ]
      },
      {
        "name": "orders",
        "description": "Stores order information",
        "columns": [
          {
            "name": "order_id",
            "type": "BIGINT",
            "is_nullable": false,
            "constraints": ["PRIMARY KEY"],
            "description": "Unique identifier for order"
          },
          {
            "name": "customer_id",
            "type": "BIGINT",
            "is_nullable": false,
            "constraints": ["FOREIGN KEY"],
            "description": "Reference to customers table"
          },
          {
            "name": "delivery_address_id",
            "type": "BIGINT",
            "is_nullable": false,
            "constraints": ["FOREIGN KEY"],
            "description": "Reference to customer_addresses table"
          },
          {
            "name": "order_status",
            "type": "VARCHAR(20)",
            "is_nullable": false,
            "description": "Current order status"
          },
          {
            "name": "total_amount",
            "type": "DECIMAL(10,2)",
            "is_nullable": false
          },
          {
            "name": "shipping_fee",
            "type": "DECIMAL(10,2)",
            "is_nullable": false
          },
          {
            "name": "created_at",
            "type": "TIMESTAMP",
            "is_nullable": false
          },
          {
            "name": "updated_at",
            "type": "TIMESTAMP",
            "is_nullable": false
          }
        ],
        "indexes": [
          {
            "name": "idx_orders_customer",
            "columns": ["customer_id"]
          },
          {
            "name": "idx_orders_status",
            "columns": ["order_status"]
          }
        ]
      },
      {
        "name": "shipments",
        "description": "Stores shipment tracking information",
        "columns": [
          {
            "name": "shipment_id",
            "type": "BIGINT",
            "is_nullable": false,
            "constraints": ["PRIMARY KEY"]
          },
          {
            "name": "order_id",
            "type": "BIGINT",
            "is_nullable": false,
            "constraints": ["FOREIGN KEY"]
          },
          {
            "name": "lsp_provider",
            "type": "VARCHAR(20)",
            "is_nullable": false
          },
          {
            "name": "tracking_number",
            "type": "VARCHAR(100)",
            "is_nullable": true
          },
          {
            "name": "shipment_status",
            "type": "VARCHAR(20)",
            "is_nullable": false
          },
          {
            "name": "estimated_delivery",
            "type": "TIMESTAMP",
            "is_nullable": true
          },
          {
            "name": "created_at",
            "type": "TIMESTAMP",
            "is_nullable": false
          },
          {
            "name": "updated_at",
            "type": "TIMESTAMP",
            "is_nullable": false
          }
        ],
        "indexes": [
          {
            "name": "idx_shipments_order",
            "columns": ["order_id"]
          },
          {
            "name": "idx_shipments_tracking",
            "columns": ["tracking_number"]
          }
        ]
      }
    ]
  },
  "reference_data": {
    "domains": [
      {
        "name": "order_statuses",
        "description": "Valid order status values",
        "values": [
          {
            "code": "CREATED",
            "description": "Order has been created",
            "is_active": true,
            "sort_order": 1
          },
          {
            "code": "PAYMENT_PENDING",
            "description": "Awaiting payment confirmation",
            "is_active": true,
            "sort_order": 2
          },
          {
            "code": "CONFIRMED",
            "description": "Order confirmed and paid",
            "is_active": true,
            "sort_order": 3
          },
          {
            "code": "PROCESSING",
            "description": "Order is being processed",
            "is_active": true,
            "sort_order": 4
          },
          {
            "code": "SHIPPED",
            "description": "Order has been shipped",
            "is_active": true,
            "sort_order": 5
          },
          {
            "code": "DELIVERED",
            "description": "Order has been delivered",
            "is_active": true,
            "sort_order": 6
          },
          {
            "code": "CANCELLED",
            "description": "Order has been cancelled",
            "is_active": true,
            "sort_order": 7
          }
        ]
      },
      {
        "name": "shipment_statuses",
        "description": "Valid shipment status values",
        "values": [
          {
            "code": "PENDING",
            "description": "Shipment created but not picked up",
            "is_active": true,
            "sort_order": 1
          },
          {
            "code": "PICKED_UP",
            "description": "Shipment collected by LSP",
            "is_active": true,
            "sort_order": 2
          },
          {
            "code": "IN_TRANSIT",
            "description": "Shipment is in transit",
            "is_active": true,
            "sort_order": 3
          },
          {
            "code": "OUT_FOR_DELIVERY",
            "description": "Shipment is out for delivery",
            "is_active": true,
            "sort_order": 4
          },
          {
            "code": "DELIVERED",
            "description": "Shipment has been delivered",
            "is_active": true,
            "sort_order": 5
          },
          {
            "code": "FAILED",
            "description": "Delivery attempt failed",
            "is_active": true,
            "sort_order": 6
          }
        ]
      },
      {
        "name": "shipping_methods",
        "description": "Available shipping methods",
        "values": [
          {
            "code": "STANDARD",
            "description": "Standard shipping (3-5 business days)",
            "base_fee": 5.99,
            "is_active": true
          },
          {
            "code": "EXPRESS",
            "description": "Express shipping (1-2 business days)",
            "base_fee": 12.99,
            "is_active": true
          }
        ]
      }
    ]
  },
  "apis": {
    "Order Management API": {
      "version": "1.0.0",
      "base_path": "/api/v1",
      "endpoints": [
        {
          "path": "/orders",
          "method": "POST",
          "description": "Create new order",
          "request_schema": {
            "type": "object",
            "properties": {
              "customer_id": {
                "type": "string",
                "description": "Unique identifier of the customer"
              },
              "delivery_address_id": {
                "type": "string",
                "description": "ID of the delivery address"
              },
              "shipping_method": {
                "type": "string",
                "enum": ["STANDARD", "EXPRESS"],
                "description": "Selected shipping method"
              },
              "items": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "product_id": {"type": "string"},
                    "quantity": {"type": "integer"}
                  }
                }
              }
            }
          },
          "response_schema": {
            "type": "object",
            "properties": {
              "order_id": {"type": "string"},
              "estimated_delivery": {"type": "string", "format": "date-time"},
              "shipping_fee": {"type": "number"},
              "total_amount": {"type": "number"}
            }
          }
        }
      ]
    }
  }
}



{
  "metadata": {
    "title": "Same-Day Delivery Service Implementation",
    "version": "1.0",
    "status": "DRAFT",
    "prepared_by": "Enterprise Architecture Team",
    "last_updated": "2025-01-13"
  },
  "sections": {
    "executive_summary": {
      "content": "This solution design outlines the implementation of same-day delivery capabilities for our e-commerce platform. The feature will enable customers to select preferred delivery windows for same-day delivery when ordering before the daily cutoff time of 1 PM."
    },
    "business_context": {
      "business_drivers": {
        "content": "Market analysis shows that 67% of customers prefer same-day delivery options when available. Customer feedback indicates delivery speed is a top factor in purchase decisions."
      },
      "constraints": {
        "content": "- Daily cutoff time of 1 PM for same-day delivery orders\n- Initial rollout limited to major metropolitan areas\n- LSP capacity limitations during peak hours"
      }
    },
    "solution_overview": {
      "high_level_design": {
        "content": "The same-day delivery service will integrate with our existing e-commerce platform, introducing new components for delivery window management and LSP integration. The solution requires changes to our existing data model, APIs, and the introduction of new delivery window concepts.",
        "required_changes": {
          "content": "1. Data Model Updates:\n- Create new 'delivery_windows' table to manage time slots and capacity\n- Add delivery window reference and type to existing orders table\n- Add zone information to customer addresses\n\n2. API Modifications:\n- Extend Order API to include delivery window selection\n- New endpoint for checking delivery window availability\n- New endpoint for LSP capacity verification\n\n3. Reference Data:\n- Add same-day delivery as a new delivery type\n- Define standard delivery windows (Morning, Afternoon, Evening)"
        }
      },
      "component_architecture": {
        "content": "1. Delivery Window Manager:\n- Manages available delivery windows and capacity\n- Handles cutoff time rules\n\n2. LSP Integration Service:\n- Real-time communication with LSP systems\n- Capacity verification and booking"
      }
    },
    "technical_architecture": {
      "data_architecture": {
        "content": "The solution requires the following data model changes:\n\n1. New Table: delivery_windows\n- window_id (Primary Key)\n- time_slot (e.g., 'MORNING', 'AFTERNOON', 'EVENING')\n- capacity\n- date\n- status\n\n2. Orders Table Updates:\n- Add delivery_window_id (Foreign Key)\n- Add delivery_type (STANDARD, EXPRESS, SAME_DAY)\n\n3. Reference Data Updates:\n- Add same-day delivery windows\n- Add delivery type codes"
      },
      "integration_architecture": {
        "content": "API changes include:\n\n1. Modified Order Management API:\n- Add deliveryWindowId to order creation\n- Add deliveryType to order options\n\n2. New Delivery Window API:\n- GET /delivery-windows/availability\n- POST /delivery-windows/reserve\n\n3. LSP Integration API:\n- Check capacity\n- Book delivery slot"
      }
    },
    "implementation_approach": {
      "phases": {
        "content": "Phase 1 (POC):\n- Implement basic delivery window management\n- Modify order creation flow\n- Basic LSP integration\n\nPhase 2 (Future):\n- Enhanced tracking capabilities\n- Dynamic pricing\n- Extended zone coverage"
      }
    },
    "non_functional_requirements": {
      "performance": {
        "content": "- API response time < 200ms for availability checks\n- Support for 100 concurrent users during POC"
      }
    }
  }
}
