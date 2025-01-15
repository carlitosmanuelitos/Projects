
________________________________________________________________________________________________________________________________________________________________________


// model_config_claude_haiku.json
{
  "model": {
    "id": "anthropic.claude-3-haiku-20240307-v1:0",
    "max_tokens": 2048,
    "temperature": 0.1,
    "top_p": 0.9,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
  },
  "retry_config": {
    "max_retries": 3,
    "initial_delay": 1,
    "max_delay": 10,
    "exponential_backoff": true
  },
  "output_format": {
    "response_format": "json",
    "include_source_references": true,
    "include_confidence_scores": true
  },
  "logging": {
    "level": "INFO",
    "include_prompts": true,
    "include_responses": true,
    "log_format": "json"
  }
}

________________________________________________________________________________________________________________________________________________________________________

// persona_config.json
{
    "content": {
        "role_definition": "You are Data-Genie, a Senior Data Architect specialized in E-commerce data environments. Your expertise covers physical data modeling, data quality management, reference data governance, and API integration patterns.",
        "context": "You operate within an E-commerce ecosystem focusing on creating comprehensive Data Impact Assessments for new IT features.",
        "primary_responsibility": "Generate detailed Data Impact Assessments that analyze and document potential changes to the data environment.",
        "analysis_approach": "Provide structured, systematic analysis breaking down impacts by specific data domains and components."
    },
    "objectives": {
        "primary": [
            {
                "id": "DIA_CREATION",
                "name": "Create Data Impact Assessments",
                "description": "Generate comprehensive DIAs for new features",
                "deliverables": [
                    "Impact summary",
                    "Detailed analysis by domain",
                    "Risk assessment",
                    "Implementation recommendations"
                ]
            },
            {
                "id": "PDM_ANALYSIS",
                "name": "Analyze Physical Data Model Impact",
                "description": "Evaluate changes needed in database schemas",
                "focus_areas": [
                    "Table structures",
                    "Relationships",
                    "Indexes",
                    "Constraints"
                ]
            },
            {
                "id": "DQ_RULES",
                "name": "Evaluate Data Quality Impact & Rules",
                "description": "Assess impact on data quality rules and controls",
                "components": [
                    "Validation rules",
                    "Monitoring requirements",
                    "Quality metrics",
                    "Cleansing procedures"
                ]
            },
            {
                "id": "REF_DATA",
                "name": "Assess Reference Data Impact",
                "description": "Analyze changes needed in reference data",
                "aspects": [
                    "Code tables",
                    "Lookup data",
                    "Classifications",
                    "Hierarchies"
                ]
            },
            {
                "id": "INTEGRATION",
                "name": "Review Data Integration Flows & API's",
                "description": "Evaluate impact on data movement and interfaces",
                "considerations": [
                    "API contracts",
                    "Data flow patterns",
                    "Integration points",
                    "Payload structures"
                ]
            }
        ],
        "constraints": [
            "Must maintain data consistency",
            "Ensure backward compatibility",
            "Follow data governance standards",
            "Preserve data lineage"
        ]
    },
    "metadata": {
        "version": "1.2",
        "last_updated": "2025-01-14",
        "author": "Data Team",
        "role": "Senior Data Architect",
        "domain": "E-commerce",
        "review_cycle": "Quarterly"
    },
    "output_preferences": {
        "format": "structured",
        "detail_level": "comprehensive",
        "include_diagrams": true,
        "highlight_critical_impacts": true
    }
}


________________________________________________________________________________________________________________________________________________________________________
data_artifacts.json: 
{"apis":{"Order Management API":{"version":"1.0.0","base_path":"/api/v1","endpoints":{"/orders":{"method":"POST","description":"Create new order","request_schema":{"type":"object","properties":{"customer_id":{"type":"string","description":"Unique identifier of the customer"},"delivery_address_id":{"type":"string","description":"ID of the delivery address"},"shipping_method":{"type":"string","enum":["STANDARD","EXPRESS"],"description":"Selected shipping method"},"items":{"type":"array","items":{"type":"object","properties":{"product_id":{"type":"string"},"quantity":{"type":"integer"}}}}}},"response_schema":{"type":"object","properties":{"order_id":{"type":"string"},"estimated_delivery":{"type":"string","format":"date-time"},"shipping_fee":{"type":"number"},"total_amount":{"type":"number"}}}}}}},"physical_data_model":{"tables":{"db_customers":{"description":"Stores customer information and delivery addresses","columns":{"customer_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for customer"},"email":{"type":"VARCHAR(255)","is_nullable":false,"description":"Customer email address"},"created_at":{"type":"TIMESTAMP","is_nullable":false},"updated_at":{"type":"TIMESTAMP","is_nullable":false}}},"db_customer_addresses":{"description":"Stores customer delivery addresses","columns":{"address_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for address"},"customer_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to customers table"},"address_line1":{"type":"VARCHAR(100)","is_nullable":false},"address_line2":{"type":"VARCHAR(100)","is_nullable":true},"city":{"type":"VARCHAR(50)","is_nullable":false},"postal_code":{"type":"VARCHAR(10)","is_nullable":false},"country":{"type":"VARCHAR(2)","is_nullable":false,"description":"ISO country code"},"is_default":{"type":"BOOLEAN","is_nullable":false,"default":false}}},"db_orders":{"description":"Stores order information","columns":{"order_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for order"},"customer_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to customers table"},"delivery_address_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to customer_addresses table"},"order_status":{"type":"VARCHAR(20)","is_nullable":false,"description":"Current order status"},"total_amount":{"type":"DECIMAL(10,2)","is_nullable":false},"payment_method":{"type":"VARCHAR(20)","is_nullable":false,"description":"Payment method used for the order"},"created_at":{"type":"TIMESTAMP","is_nullable":false},"updated_at":{"type":"TIMESTAMP","is_nullable":false}}},"db_shipments":{"description":"Stores shipment tracking information","columns":{"shipment_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"]},"order_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"]},"lsp_provider":{"type":"VARCHAR(20)","is_nullable":false},"tracking_number":{"type":"VARCHAR(100)","is_nullable":true},"shipment_status":{"type":"VARCHAR(20)","is_nullable":false},"shipping_method":{"type":"VARCHAR(20)","is_nullable":false,"description":"Shipping method used for the shipment"},"estimated_delivery":{"type":"TIMESTAMP","is_nullable":true},"created_at":{"type":"TIMESTAMP","is_nullable":false},"updated_at":{"type":"TIMESTAMP","is_nullable":false}}},"db_products":{"description":"Stores product information","columns":{"product_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for product"},"product_name":{"type":"VARCHAR(255)","is_nullable":false,"description":"Name of the product"},"price":{"type":"DECIMAL(10,2)","is_nullable":false,"description":"Price of the product"},"product_category":{"type":"VARCHAR(50)","is_nullable":false,"description":"Category of the product"},"created_at":{"type":"TIMESTAMP","is_nullable":false,"description":"Record creation timestamp"}}},"db_order_items":{"description":"Stores order items information","columns":{"order_item_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for order item"},"order_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to orders table"},"product_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to products table"},"quantity":{"type":"INTEGER","is_nullable":false,"description":"Quantity of the product ordered"},"price":{"type":"DECIMAL(10,2)","is_nullable":false,"description":"Price of the product at the time of order"}}}}},"reference_data":{"domains":{"rd_order_statuses":{"description":"Valid order status values","values":{"CREATED":{"description":"Order has been created","is_active":true,"sort_order":1},"PAYMENT_PENDING":{"description":"Awaiting payment confirmation","is_active":true,"sort_order":2},"PROCESSING":{"description":"Order is being processed","is_active":true,"sort_order":3},"SHIPPED":{"description":"Order has been shipped","is_active":true,"sort_order":4},"DELIVERED":{"description":"Order has been delivered","is_active":true,"sort_order":5},"CANCELLED":{"description":"Order has been cancelled","is_active":true,"sort_order":6},"Undelivered":{"description":"Order has been undelivered","is_active":true,"sort_order":7}}},"rd_shipment_statuses":{"description":"Valid shipment status values","values":{"PENDING":{"description":"Shipment created but not picked up","is_active":true,"sort_order":1},"IN_TRANSIT":{"description":"Shipment is in transit","is_active":true,"sort_order":2},"DELIVERED":{"description":"Shipment has been delivered","is_active":true,"sort_order":3},"FAILED":{"description":"Delivery attempt failed","is_active":true,"sort_order":4}}},"rd_shipping_methods":{"description":"Available shipping methods","values":{"STANDARD":{"description":"Standard shipping (3-5 business days)","base_fee":5.99,"is_active":true},"EXPRESS":{"description":"Express shipping (1-2 business days)","base_fee":12.99,"is_active":true}}},"rd_product_categories":{"description":"Valid product categories","values":{"CONSUMABLES":{"description":"Consumables - Heets and Terea","is_active":true,"sort_order":1},"DEVICES":{"description":"Devices and Kits","is_active":true,"sort_order":2},"BUNDLES":{"description":"Bundles - combination of device and consumables","is_active":true,"sort_order":3}}},"rd_payment_methods":{"description":"Available payment methods","values":{"CREDIT_CARD":{"description":"Credit card payment","is_active":true,"sort_order":1},"BANK_TRANSFER":{"description":"Bank transfer payment","is_active":true,"sort_order":2},"CASH_ON_DELIVERY":{"description":"Cash on delivery","is_active":true,"sort_order":3}}}}},"metadata":{"version":"v2","last_updated":"2025-01-14T18:42:18.919392","source_checksums":{"api_documentation.json":"467c7b22197dee1c5da44bcb3269f29c","physical_data_model.json":"7b8b04f2976616ea012d5fa1e42c8001","reference_data.json":"0d70626a330b6a7de391029656191f3c"}}}

________________________________________________________________________________________________________________________________________________________________________


# Initialize the analyzer
analyzer = DIAAnalyzer('configs/persona_config_v2.json', 'configs/model_config_claude_haiku_v2.json')
        
# Load the input data
with open('data_input/input_data_ad_ai.json', 'r') as f:
    ad_content = json.load(f)
    logger.info("Successfully loaded input data")

# Set objectives and load context
analyzer.set_active_objectives(['PDM_ANALYSIS'])
analyzer.load_context(ad_content)

# Run analysis
result = analyzer.analyze_prompt(
    "Analyze the physical data model changes required for this implementation. "
    "Include impact on existing tables and new table requirements."
    )

# Print formatted results
analyzer.print_results(result)

# Example of accessing prompt and metrics
print("\nLatest Prompt:")
latest_prompt = analyzer.get_latest_prompt()
print(latest_prompt['prompt'] if latest_prompt else "No prompt available")









# Example 1: Focus on PDM Analysis only
analyzer.set_active_objectives(['PDM_ANALYSIS'])
analyzer.load_context(ad_content)
pdm_result = analyzer.analyze_prompt(
    "Analyze the physical data model changes required for this implementation. "
    "Include impact on existing tables and new table requirements."
)

# Example 2: Focus on Integration and Reference Data
analyzer.set_active_objectives(['INTEGRATION', 'REF_DATA'])
analyzer.load_context(ad_content)
integration_result = analyzer.analyze_prompt(
    "Analyze the API changes and reference data impacts. "
    "Focus on new API endpoints and required reference data updates."
)

# Example 3: Comprehensive Analysis
analyzer.set_active_objectives(['DIA_CREATION', 'PDM_ANALYSIS', 'DQ_RULES', 'REF_DATA', 'INTEGRATION'])
analyzer.load_context(ad_content)
full_result = analyzer.analyze_prompt(
    "Provide a comprehensive data impact assessment for the same-day delivery implementation."
)

# Example 4: Data Quality Focus
analyzer.set_active_objectives(['DQ_RULES'])
analyzer.load_context(ad_content)
dq_result = analyzer.analyze_prompt(
    "Analyze the data quality implications of this implementation. "
    "Focus on required validation rules and quality controls."
)

# Example 5: PDM and Integration Combined Analysis
analyzer.set_active_objectives(['PDM_ANALYSIS', 'INTEGRATION'])
analyzer.load_context(ad_content)
pdm_api_result = analyzer.analyze_prompt(
    "Analyze how the new API endpoints will interact with the proposed database changes. "
    "Include any potential performance or consistency considerations."
)
