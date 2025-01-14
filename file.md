model_config_claude_haiku.json:
{
  "model": {
    "id": "anthropic.claude-3-haiku-20240307-v1:0",
    "max_tokens": 2048,
    "temperature": 0.1,
    "top_p": 0.9
  }
}


persona_config.json:
{
    "content": "You are Data-Genie, a Senior Data Architect. Your main objective is to create Data Impact Assessments for new IT features being built on an E-commerce environment. Focus on Physical Data Model Impact, Data Quality Housekeeping Rules, Reference Data Impact, and Data Integration Flows across different components. Please provide detailed and accurate responses breaking down each object. Your specific objectives include: Create Data Impact Assessments, Analyze Physical Data Model Impact, Evaluate Data Quality Impact & Rules, Assess Reference Data Impact, Review Data Integration Flows & API's.",
    "metadata": {
        "version": "1.1",
        "last_updated": "2025-01-06",
        "author": "Data Team",
        "role": "Senior Data Architect",
        "objectives": [
            "Create Data Impact Assessments",
            "Analyze Physical Data Model Impact",
            "Evaluate Data Quality Housekeeping Rules",
            "Assess Reference Data Impact",
            "Review Data Integration Flows & API's"
        ]
    }
}

input_ad_data.json: 
{
  "metadata": {
    "title": "Same-Day Delivery Service Implementation",
    "version": "1.1",
    "status": "DRAFT",
    "prepared_by": "Enterprise Architecture Team",
    "last_updated": "2025-01-13",
    "reviewed_by": "Technical Architecture Board"
  },
  "sections": {
    "executive_summary": {
      "content": "This solution design outlines the implementation of same-day delivery capabilities for our e-commerce platform. The feature will enable customers to select preferred delivery windows for same-day delivery when ordering before the daily cutoff time of 1 PM, with dynamic capacity management and real-time LSP integration."
    },
    "business_context": {
      "business_drivers": {
        "content": "Market analysis shows that 67% of customers prefer same-day delivery options when available. Customer feedback indicates delivery speed is a top factor in purchase decisions. Competitors have begun offering similar services, making this a critical competitive differentiator."
      },
      "constraints": {
        "content": "- Daily cutoff time of 1 PM for same-day delivery orders\n- Initial rollout limited to major metropolitan areas\n- LSP capacity limitations during peak hours\n- Maximum package dimensions: 50x50x50 cm\n- Weight limit: 15 kg per package"
      }
    },
    "solution_overview": {
      "high_level_design": {
        "content": "The same-day delivery service will integrate with our existing e-commerce platform, introducing new components for delivery window management and LSP integration. The solution implements a microservices architecture with event-driven communication for real-time updates.",
        "required_changes": {
          "content": "1. Data Model Updates:\n- Create new 'delivery_windows' table for time slot management\n- Create new 'delivery_zones' table for geographic coverage\n- Create new 'lsp_capacity' table for real-time capacity tracking\n- Add delivery window reference and type to existing orders table\n- Add zone information to customer addresses\n\n2. API Modifications:\n- Extend Order API to include delivery window selection\n- New endpoint for checking delivery window availability\n- New endpoint for LSP capacity verification\n- New webhook endpoints for LSP status updates\n\n3. Reference Data:\n- Add same-day delivery as a new delivery type\n- Define standard delivery windows (Morning: 9AM-1PM, Afternoon: 1PM-5PM, Evening: 5PM-9PM)\n- Define zone codes and mapping to postal codes"
        }
      },
      "component_architecture": {
        "content": "1. Delivery Window Manager:\n- Manages available delivery windows and capacity\n- Handles cutoff time rules\n- Implements capacity forecasting algorithms\n\n2. LSP Integration Service:\n- Real-time communication with LSP systems\n- Capacity verification and booking\n- Status update processing\n\n3. Zone Management Service:\n- Handles geographic coverage rules\n- Manages delivery zone assignments\n\n4. Pricing Engine:\n- Calculates delivery fees based on zones and time slots\n- Handles surge pricing during peak periods"
      }
    },
    "technical_architecture": {
      "data_architecture": {
        "content": "Detailed data model changes:\n\n1. New Table: delivery_windows\n- window_id (UUID, Primary Key)\n- time_slot_code (VARCHAR, e.g., 'MORNING', 'AFTERNOON', 'EVENING')\n- start_time (TIMESTAMP)\n- end_time (TIMESTAMP)\n- base_capacity (INTEGER)\n- available_capacity (INTEGER)\n- zone_id (UUID, Foreign Key)\n- date (DATE)\n- status (VARCHAR: OPEN, CLOSED, FULL)\n- created_at (TIMESTAMP)\n- updated_at (TIMESTAMP)\n\n2. New Table: delivery_zones\n- zone_id (UUID, Primary Key)\n- zone_code (VARCHAR)\n- zone_name (VARCHAR)\n- postal_code_pattern (VARCHAR)\n- is_active (BOOLEAN)\n- service_level (VARCHAR: PREMIUM, STANDARD)\n- created_at (TIMESTAMP)\n- updated_at (TIMESTAMP)\n\n3. New Table: lsp_capacity\n- capacity_id (UUID, Primary Key)\n- lsp_id (UUID, Foreign Key)\n- zone_id (UUID, Foreign Key)\n- window_id (UUID, Foreign Key)\n- total_capacity (INTEGER)\n- reserved_capacity (INTEGER)\n- last_updated (TIMESTAMP)\n\n4. Orders Table Updates:\n- Add delivery_window_id (UUID, Foreign Key)\n- Add delivery_zone_id (UUID, Foreign Key)\n- Add delivery_type (VARCHAR: STANDARD, EXPRESS, SAME_DAY)\n- Add lsp_tracking_ref (VARCHAR)\n- Add delivery_status (VARCHAR)\n\n5. Customer_addresses Table Updates:\n- Add zone_id (UUID, Foreign Key)\n- Add zone_validation_date (TIMESTAMP)"
      },
      "integration_architecture": {
        "content": "API changes include:\n\n1. Modified Order Management API:\n- POST /orders/create (updated)\n  - Add deliveryWindowId\n  - Add deliveryType\n  - Add zoneId\n\n2. New Delivery Window API:\n- GET /delivery-windows/availability\n  - Query params: postalCode, date\n- POST /delivery-windows/reserve\n- DELETE /delivery-windows/release\n\n3. LSP Integration API:\n- POST /lsp/verify-capacity\n- POST /lsp/book-delivery\n- POST /lsp/cancel-delivery\n- POST /webhooks/lsp/status-update\n\n4. Zone Management API:\n- GET /zones/validate-address\n- GET /zones/coverage"
      }
    },
    "implementation_approach": {
      "phases": {
        "content": "Phase 1 (POC):\n- Core delivery window management\n- Basic LSP integration\n- Initial zone coverage for two metropolitan areas\n\nPhase 2 (MVP):\n- Enhanced tracking capabilities\n- Basic dynamic pricing\n- Extended zone coverage\n- Multi-LSP support\n\nPhase 3 (Scale):\n- Advanced analytics and forecasting\n- Automated capacity optimization\n- Full dynamic pricing implementation"
      }
    },
    "non_functional_requirements": {
      "performance": {
        "content": "- API response time < 200ms for availability checks\n- Support for 1000 concurrent users\n- Maximum 1.5s for end-to-end order creation\n- 99.9% uptime for core services\n- Maximum 5s for LSP integration operations"
      },
      "scaling": {
        "content": "- Horizontal scaling for all services\n- Cache hit ratio > 85% for delivery window queries\n- Maximum 100ms latency for cache operations"
      }
    }
  }
}

data_artifacts.json: 
{"apis":{"Order Management API":{"version":"1.0.0","base_path":"/api/v1","endpoints":{"/orders":{"method":"POST","description":"Create new order","request_schema":{"type":"object","properties":{"customer_id":{"type":"string","description":"Unique identifier of the customer"},"delivery_address_id":{"type":"string","description":"ID of the delivery address"},"shipping_method":{"type":"string","enum":["STANDARD","EXPRESS"],"description":"Selected shipping method"},"items":{"type":"array","items":{"type":"object","properties":{"product_id":{"type":"string"},"quantity":{"type":"integer"}}}}}},"response_schema":{"type":"object","properties":{"order_id":{"type":"string"},"estimated_delivery":{"type":"string","format":"date-time"},"shipping_fee":{"type":"number"},"total_amount":{"type":"number"}}}}}}},"physical_data_model":{"tables":{"db_customers":{"description":"Stores customer information and delivery addresses","columns":{"customer_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for customer"},"email":{"type":"VARCHAR(255)","is_nullable":false,"description":"Customer email address"},"created_at":{"type":"TIMESTAMP","is_nullable":false},"updated_at":{"type":"TIMESTAMP","is_nullable":false}}},"db_customer_addresses":{"description":"Stores customer delivery addresses","columns":{"address_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for address"},"customer_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to customers table"},"address_line1":{"type":"VARCHAR(100)","is_nullable":false},"address_line2":{"type":"VARCHAR(100)","is_nullable":true},"city":{"type":"VARCHAR(50)","is_nullable":false},"postal_code":{"type":"VARCHAR(10)","is_nullable":false},"country":{"type":"VARCHAR(2)","is_nullable":false,"description":"ISO country code"},"is_default":{"type":"BOOLEAN","is_nullable":false,"default":false}}},"db_orders":{"description":"Stores order information","columns":{"order_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for order"},"customer_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to customers table"},"delivery_address_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to customer_addresses table"},"order_status":{"type":"VARCHAR(20)","is_nullable":false,"description":"Current order status"},"total_amount":{"type":"DECIMAL(10,2)","is_nullable":false},"payment_method":{"type":"VARCHAR(20)","is_nullable":false,"description":"Payment method used for the order"},"created_at":{"type":"TIMESTAMP","is_nullable":false},"updated_at":{"type":"TIMESTAMP","is_nullable":false}}},"db_shipments":{"description":"Stores shipment tracking information","columns":{"shipment_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"]},"order_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"]},"lsp_provider":{"type":"VARCHAR(20)","is_nullable":false},"tracking_number":{"type":"VARCHAR(100)","is_nullable":true},"shipment_status":{"type":"VARCHAR(20)","is_nullable":false},"shipping_method":{"type":"VARCHAR(20)","is_nullable":false,"description":"Shipping method used for the shipment"},"estimated_delivery":{"type":"TIMESTAMP","is_nullable":true},"created_at":{"type":"TIMESTAMP","is_nullable":false},"updated_at":{"type":"TIMESTAMP","is_nullable":false}}},"db_products":{"description":"Stores product information","columns":{"product_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for product"},"product_name":{"type":"VARCHAR(255)","is_nullable":false,"description":"Name of the product"},"price":{"type":"DECIMAL(10,2)","is_nullable":false,"description":"Price of the product"},"product_category":{"type":"VARCHAR(50)","is_nullable":false,"description":"Category of the product"},"created_at":{"type":"TIMESTAMP","is_nullable":false,"description":"Record creation timestamp"}}},"db_order_items":{"description":"Stores order items information","columns":{"order_item_id":{"type":"BIGINT","is_nullable":false,"constraints":["PRIMARY KEY"],"description":"Unique identifier for order item"},"order_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to orders table"},"product_id":{"type":"BIGINT","is_nullable":false,"constraints":["FOREIGN KEY"],"description":"Reference to products table"},"quantity":{"type":"INTEGER","is_nullable":false,"description":"Quantity of the product ordered"},"price":{"type":"DECIMAL(10,2)","is_nullable":false,"description":"Price of the product at the time of order"}}}}},"reference_data":{"domains":{"rd_order_statuses":{"description":"Valid order status values","values":{"CREATED":{"description":"Order has been created","is_active":true,"sort_order":1},"PAYMENT_PENDING":{"description":"Awaiting payment confirmation","is_active":true,"sort_order":2},"PROCESSING":{"description":"Order is being processed","is_active":true,"sort_order":3},"SHIPPED":{"description":"Order has been shipped","is_active":true,"sort_order":4},"DELIVERED":{"description":"Order has been delivered","is_active":true,"sort_order":5},"CANCELLED":{"description":"Order has been cancelled","is_active":true,"sort_order":6},"Undelivered":{"description":"Order has been undelivered","is_active":true,"sort_order":7}}},"rd_shipment_statuses":{"description":"Valid shipment status values","values":{"PENDING":{"description":"Shipment created but not picked up","is_active":true,"sort_order":1},"IN_TRANSIT":{"description":"Shipment is in transit","is_active":true,"sort_order":2},"DELIVERED":{"description":"Shipment has been delivered","is_active":true,"sort_order":3},"FAILED":{"description":"Delivery attempt failed","is_active":true,"sort_order":4}}},"rd_shipping_methods":{"description":"Available shipping methods","values":{"STANDARD":{"description":"Standard shipping (3-5 business days)","base_fee":5.99,"is_active":true},"EXPRESS":{"description":"Express shipping (1-2 business days)","base_fee":12.99,"is_active":true}}},"rd_product_categories":{"description":"Valid product categories","values":{"CONSUMABLES":{"description":"Consumables - Heets and Terea","is_active":true,"sort_order":1},"DEVICES":{"description":"Devices and Kits","is_active":true,"sort_order":2},"BUNDLES":{"description":"Bundles - combination of device and consumables","is_active":true,"sort_order":3}}},"rd_payment_methods":{"description":"Available payment methods","values":{"CREDIT_CARD":{"description":"Credit card payment","is_active":true,"sort_order":1},"BANK_TRANSFER":{"description":"Bank transfer payment","is_active":true,"sort_order":2},"CASH_ON_DELIVERY":{"description":"Cash on delivery","is_active":true,"sort_order":3}}}}},"metadata":{"version":"v2","last_updated":"2025-01-14T18:42:18.919392","source_checksums":{"api_documentation.json":"467c7b22197dee1c5da44bcb3269f29c","physical_data_model.json":"7b8b04f2976616ea012d5fa1e42c8001","reference_data.json":"0d70626a330b6a7de391029656191f3c"}}}


model_initiation_claude.ipynb:
import boto3
import json
import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the default logging level to INFO
logger = logging.getLogger(__name__)
logging.getLogger('botocore').setLevel(logging.WARNING)

class DIAAnalyzer:
    def __init__(self, persona_path: str, model_config_path: str):
        # Initialize AWS clients with region specification
        logger.debug("Initializing AWS Bedrock client")
        self.bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
        
        # Load configurations
        logger.debug(f"Loading model configuration from {model_config_path}")
        self.model_config = self._load_model_config(model_config_path)
        self.model_id = self.model_config['model']['id']
        
        # Load persona instructions
        logger.debug(f"Loading persona instructions from {persona_path}")
        self.persona, self.objectives = self._load_persona(persona_path)
        
        # Initialize context as None
        self.context = None

    def _load_model_config(self, model_config_path: str) -> Dict:
        """Load model configuration."""
        logger.debug(f"Reading model configuration file: {model_config_path}")
        with open(model_config_path, 'r') as f:
            config = json.load(f)
        logger.debug(f"Model configuration loaded: {config}")
        return config

    def _load_persona(self, persona_path: str) -> (str, list):
        """Load the Data Architect persona instructions from a JSON file."""
        logger.debug(f"Reading persona configuration file: {persona_path}")
        with open(persona_path, 'r') as f:
            persona_config = json.load(f)
        logger.debug(f"Persona instructions loaded: {persona_config['content']}")
        return persona_config['content'], persona_config['metadata']['objectives']

    def load_context(self, context_path: str) -> None:
        """Load context from a JSON file."""
        try:
            logger.debug(f"Loading context from {context_path}")
            with open(context_path, 'r') as f:
                self.context = json.load(f)
            logger.debug("Context loaded successfully")
        except Exception as e:
            logger.error(f"Error loading context: {e}")
            raise

    def _create_prompt(self, prompt: str) -> str:
        """Create the full prompt combining persona and user prompt."""
        objectives_text = "Your specific objectives include: " + ", ".join(self.objectives) + "."
        
        # Add context if available
        context_text = ""
        if self.context:
            context_text = f"\nAvailable Context:\n{json.dumps(self.context, indent=2)}"
        
        full_prompt = f"""
        {self.persona}
        {objectives_text}
    
        Please analyze the following prompt and provide a detailed response:
        {prompt}
        {context_text}
        """
        logger.debug(f"Full prompt created: {full_prompt}")
        return full_prompt

    def analyze_prompt(self, prompt: str) -> Dict:
        """Main method to analyze a prompt and generate a response."""
        # Create full prompt
        full_prompt = self._create_prompt(prompt)
        
        # Call Bedrock model
        try:
            logger.debug("Invoking Bedrock model")
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                contentType='application/json',
                accept='application/json',
                body=json.dumps({
                    "messages": [
                        {"role": "user", "content": full_prompt}
                    ],
                    "max_tokens": self.model_config['model']['max_tokens'],
                    "temperature": self.model_config['model']['temperature'],
                    "top_p": self.model_config['model']['top_p'],
                    "anthropic_version": 'bedrock-2023-05-31'
                })
            )
            logger.debug("Model invoked successfully")
        except Exception as e:
            logger.error(f"Error invoking model: {e}")
            raise
        
        # Parse and return the response
        try:
            logger.debug("Parsing model response")
            model_response = json.loads(response['body'].read())
            logger.debug(f"Model response parsed successfully")
            return self._extract_valuable_info(model_response)
        except Exception as e:
            logger.error(f"Error parsing model response: {e}")
            raise

    def _extract_valuable_info(self, model_response: Dict) -> Dict:
        """Extract the valuable information from the model response."""
        content_text = model_response['content'][0]['text']
        input_tokens = model_response['usage']['input_tokens']
        output_tokens = model_response['usage']['output_tokens']
        
        return {
            "content_text": content_text,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens
        }

    def _format_response(self, response: Dict) -> str:
        """Format the response in Markdown."""
        formatted_response = f"""
## Data Impact Assessment Output Example:

{response['content_text']}

**Input Tokens:** {response['input_tokens']}  
**Output Tokens:** {response['output_tokens']}
"""
        return formatted_response




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


import boto3
import json
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.getLogger('botocore').setLevel(logging.WARNING)

class DIAAnalyzer:
    def __init__(self, persona_path: str, model_config_path: str):
        """Initialize the DIA Analyzer with persona and model configurations."""
        logger.debug("Initializing AWS Bedrock client")
        self.bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
        
        # Load configurations
        self.model_config = self._load_json_file(model_config_path)
        self.model_id = self.model_config['model']['id']
        
        # Load and structure persona config
        self.persona_config = self._load_json_file(persona_path)
        self.active_objectives = self.persona_config['objectives']['primary']
        
        # Initialize context
        self.context = None

    def _load_json_file(self, file_path: str) -> Dict:
        """Load and parse a JSON file."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading file {file_path}: {e}")
            raise

    def set_active_objectives(self, objective_ids: List[str]) -> None:
        """Set specific objectives to focus on."""
        all_objectives = {obj['id']: obj for obj in self.persona_config['objectives']['primary']}
        self.active_objectives = [
            all_objectives[obj_id] for obj_id in objective_ids
            if obj_id in all_objectives
        ]
        logger.info(f"Set active objectives: {[obj['name'] for obj in self.active_objectives]}")

    def load_context(self, context: Dict) -> None:
        """Load the analysis context directly."""
        self.context = context
        logger.debug("Context loaded successfully")

    def _create_prompt(self, prompt: str) -> str:
        """Create the analysis prompt with current context and objectives."""
        # Format objectives for clear instruction
        objectives_text = "\nFocus on the following objectives:\n"
        for obj in self.active_objectives:
            objectives_text += f"\n{obj['name']}: {obj['description']}"
            if 'components' in obj:
                objectives_text += "\nKey components to consider:"
                for component in obj['components']:
                    objectives_text += f"\n- {component}"

        # Add constraints if available
        constraints_text = ""
        if 'constraints' in self.persona_config['objectives']:
            constraints_text = "\n\nAnalysis Constraints:\n" + \
                             "\n".join(f"- {c}" for c in self.persona_config['objectives']['constraints'])

        full_prompt = f"""
{self.persona_config['content']['role_definition']}

{objectives_text}
{constraints_text}

Document Content:
{json.dumps(self.context, indent=2)}

Analysis Request:
{prompt}
"""
        return full_prompt

    def analyze_prompt(self, prompt: str) -> Dict:
        """Analyze the context with given prompt and return structured response."""
        full_prompt = self._create_prompt(prompt)
        
        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                contentType='application/json',
                accept='application/json',
                body=json.dumps({
                    "messages": [{"role": "user", "content": full_prompt}],
                    "max_tokens": self.model_config['model']['max_tokens'],
                    "temperature": self.model_config['model']['temperature'],
                    "top_p": self.model_config['model']['top_p'],
                    "anthropic_version": 'bedrock-2023-05-31'
                })
            )
            
            model_response = json.loads(response['body'].read())
            return {
                "content": model_response['content'][0]['text'],
                "metadata": {
                    "input_tokens": model_response['usage']['input_tokens'],
                    "output_tokens": model_response['usage']['output_tokens'],
                    "active_objectives": [obj['id'] for obj in self.active_objectives]
                }
            }
            
        except Exception as e:
            logger.error(f"Error in analyze_prompt: {e}")
            raise


# Initialize the analyzer
analyzer = DIAAnalyzer('persona_config.json', 'model_config_claude_haiku.json')

# Load your AD document
with open('input_ad_data.json', 'r') as f:
    ad_content = json.load(f)

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
