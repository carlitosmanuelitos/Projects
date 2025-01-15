
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

import boto3
import json
import logging
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger('botocore').setLevel(logging.WARNING)

@dataclass
class ModelMetrics:
    """Class to store model execution metrics"""
    input_tokens: int
    output_tokens: int
    total_tokens: int
    execution_time: float
    timestamp: str

class PromptTracker:
    """Class to track and store prompts"""
    def __init__(self):
        self.prompts = []
        
    def add_prompt(self, prompt: str, timestamp: str):
        self.prompts.append({
            "prompt": prompt,
            "timestamp": timestamp
        })
    
    def get_latest_prompt(self) -> Dict:
        return self.prompts[-1] if self.prompts else None
    
    def get_all_prompts(self) -> List[Dict]:
        return self.prompts

class DIAAnalyzer:
    def __init__(self, persona_path: str, model_config_path: str):
        """Initialize the DIA Analyzer with persona and model configurations."""
        logger.info("Initializing DIAAnalyzer")
        self.bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
        
        # Load configurations
        self.model_config = self._load_json_file(model_config_path)
        self.model_id = self.model_config['model']['id']
        
        # Load and structure persona config
        self.persona_config = self._load_json_file(persona_path)
        self.active_objectives = self.persona_config['objectives']['primary']
        
        # Initialize tracking components
        self.prompt_tracker = PromptTracker()
        self.latest_metrics = None
        self.context = None
        
        # Initialize Rich console for pretty printing
        self.console = Console()

    def _load_json_file(self, file_path: str) -> Dict:
        """Load and parse a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                logger.info(f"Successfully loaded configuration from {file_path}")
                return data
        except Exception as e:
            logger.error(f"Error loading file {file_path}: {e}")
            raise

    def set_active_objectives(self, objective_ids: List[str]) -> None:
        """Set specific objectives to focus on."""
        all_objectives = {obj['id']: obj for obj in self.persona_config['objectives']['primary']}
        self.active_objectives = []
        
        for obj_id in objective_ids:
            if obj_id in all_objectives:
                self.active_objectives.append(all_objectives[obj_id])
                logger.info(f"Added objective: {all_objectives[obj_id]['name']}")
            else:
                logger.warning(f"Objective ID not found: {obj_id}")
        
        if not self.active_objectives:
            logger.error("No valid objectives were set")
            raise ValueError("No valid objectives were provided")

    def load_context(self, context: Dict) -> None:
        """Load the analysis context directly."""
        if not context:
            logger.error("Empty context provided")
            raise ValueError("Context cannot be empty")
            
        self.context = context
        logger.info("Context loaded successfully")
        
        
    def _create_prompt(self, prompt: str) -> str:
        """Create the analysis prompt with current context and objectives."""
        if not self.active_objectives:
            logger.error("No active objectives set")
            raise ValueError("No active objectives have been set")
            
        if not self.context:
            logger.error("No context loaded")
            raise ValueError("No context has been loaded")

        # Format objectives for clear instruction
        objectives_text = "\nFocus on the following objectives:\n"
        for obj in self.active_objectives:
            objectives_text += f"\n{obj['name']}: {obj['description']}"
            for key in ['components', 'focus_areas', 'deliverables', 'aspects', 'considerations']:
                if key in obj:
                    objectives_text += f"\nKey {key} to consider:"
                    for item in obj[key]:
                        objectives_text += f"\n- {item}"

        # Add constraints
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

Please provide a structured analysis following the objectives and constraints outlined above.
"""
        logger.debug(f"Created prompt with length: {len(full_prompt)}")
        self.prompt_tracker.add_prompt(full_prompt, datetime.datetime.now().isoformat())
        return full_prompt

    def analyze_prompt(self, prompt: str) -> Dict:
        """Analyze the context with given prompt and return structured response."""
        try:
            start_time = datetime.datetime.now()
            full_prompt = self._create_prompt(prompt)
            
            request_body = {
                "messages": [{"role": "user", "content": full_prompt}],
                "max_tokens": self.model_config['model']['max_tokens'],
                "temperature": self.model_config['model']['temperature'],
                "top_p": self.model_config['model']['top_p'],
                "anthropic_version": 'bedrock-2023-05-31'
            }
            
            logger.info("Invoking Bedrock model")
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                contentType='application/json',
                accept='application/json',
                body=json.dumps(request_body)
            )

            response_body = json.loads(response['body'].read())
            end_time = datetime.datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            # Store metrics
            self.latest_metrics = ModelMetrics(
                input_tokens=response_body['usage']['input_tokens'],
                output_tokens=response_body['usage']['output_tokens'],
                total_tokens=response_body['usage']['input_tokens'] + response_body['usage']['output_tokens'],
                execution_time=execution_time,
                timestamp=end_time.isoformat()
            )

            result = {
                "content": response_body['content'][0]['text'],
                "metadata": {
                    "input_tokens": self.latest_metrics.input_tokens,
                    "output_tokens": self.latest_metrics.output_tokens,
                    "total_tokens": self.latest_metrics.total_tokens,
                    "execution_time": self.latest_metrics.execution_time,
                    "active_objectives": [obj['id'] for obj in self.active_objectives],
                    "timestamp": self.latest_metrics.timestamp
                }
            }

            return result

        except Exception as e:
            logger.error(f"Error in analyze_prompt: {e}")
            raise

    def print_results(self, result: Dict):
        """Print analysis results in a formatted way"""
        # Print the main analysis content
        self.console.print("\n[bold blue]Analysis Result[/bold blue]")
        self.console.print(Panel(result['content'], title="Analysis Content", border_style="blue"))
        
        # Print metrics in a table
        metrics_table = Table(title="Execution Metrics", show_header=True, header_style="bold magenta")
        metrics_table.add_column("Metric", style="cyan")
        metrics_table.add_column("Value", style="green")
        
        for key, value in result['metadata'].items():
            metrics_table.add_row(key, str(value))
        
        self.console.print(metrics_table)

    def get_latest_prompt(self) -> Dict:
        """Retrieve the latest prompt used"""
        return self.prompt_tracker.get_latest_prompt()

    def get_latest_metrics(self) -> ModelMetrics:
        """Retrieve the latest execution metrics"""
        return self.latest_metrics
        
________________________________________________________________________________________________________________________________________________________________________

        
# Initialize the analyzer
analyzer = DIAAnalyzer('configs/persona_config_v2.json', 'configs/model_config_claude_haiku_v2.json')
        
# Load the input data
with open('data_input/input_data_ad_ai.json', 'r') as f:
    ad_content = json.load(f)
    logger.info("Successfully loaded input data")

# Example 1: PDM Analysis
analyzer.set_active_objectives(['PDM_ANALYSIS'])
analyzer.load_context(ad_content)

# Run analysis
result = analyzer.analyze_prompt(
    "Analyze the physical data model changes required for this implementation. "
    "Include impact on existing tables and new table requirements."
    )

# Example of accessing prompt and metrics
print("\nLatest Prompt:")
latest_prompt = analyzer.get_latest_prompt()
print(latest_prompt['prompt'] if latest_prompt else "No prompt available")

# Print formatted results
analyzer.print_results(result)

________________________________________________________________________________________________________________________________________________________________________

Analysis Result
╭─────────────────────────────────────────────── Analysis Content ────────────────────────────────────────────────╮
│ As a Senior Data Architect specialized in E-commerce data environments, I have analyzed the physical data model │
│ changes required for the implementation of the same-day delivery service. The analysis considers the key focus  │
│ areas, including table structures, relationships, indexes, and constraints, while ensuring data consistency,    │
│ backward compatibility, data governance standards, and data lineage preservation.                               │
│                                                                                                                 │
│ 1. Table Structures:                                                                                            │
│                                                                                                                 │
│    a. New Tables:                                                                                               │
│       - `delivery_windows`: This table will manage the available delivery time slots, including the time slot   │
│ code, start and end times, base capacity, available capacity, zone information, date, and status.               │
│       - `delivery_zones`: This table will store the details of the geographic delivery zones, such as the zone  │
│ code, name, postal code pattern, service level, and active status.                                              │
│       - `lsp_capacity`: This table will track the real-time capacity information for each delivery zone and     │
│ time slot, including the total and reserved capacity.                                                           │
│                                                                                                                 │
│    b. Existing Table Updates:                                                                                   │
│       - `orders`: Add new columns for `delivery_window_id`, `delivery_zone_id`, `delivery_type`,                │
│ `lsp_tracking_ref`, and `delivery_status`.                                                                      │
│       - `customer_addresses`: Add a new column for `zone_id` and `zone_validation_date`.                        │
│                                                                                                                 │
│ 2. Relationships:                                                                                               │
│                                                                                                                 │
│    a. `delivery_windows` table:                                                                                 │
│       - `zone_id` column is a foreign key referencing the `delivery_zones` table.                               │
│                                                                                                                 │
│    b. `lsp_capacity` table:                                                                                     │
│       - `zone_id` column is a foreign key referencing the `delivery_zones` table.                               │
│       - `window_id` column is a foreign key referencing the `delivery_windows` table.                           │
│       - `lsp_id` column is a foreign key referencing an external LSP (Logistics Service Provider) table.        │
│                                                                                                                 │
│    c. `orders` table:                                                                                           │
│       - `delivery_window_id` column is a foreign key referencing the `delivery_windows` table.                  │
│       - `delivery_zone_id` column is a foreign key referencing the `delivery_zones` table.                      │
│                                                                                                                 │
│    d. `customer_addresses` table:                                                                               │
│       - `zone_id` column is a foreign key referencing the `delivery_zones` table.                               │
│                                                                                                                 │
│ 3. Indexes:                                                                                                     │
│                                                                                                                 │
│    a. `delivery_windows` table:                                                                                 │
│       - Index on `zone_id`, `date`, `time_slot_code`, and `status` columns for efficient delivery window        │
│ availability checks.                                                                                            │
│                                                                                                                 │
│    b. `delivery_zones` table:                                                                                   │
│       - Index on `zone_code` and `postal_code_pattern` columns for fast zone lookup and validation.             │
│                                                                                                                 │
│    c. `lsp_capacity` table:                                                                                     │
│       - Index on `zone_id`, `window_id`, and `last_updated` columns for quick capacity verification and         │
│ updates.                                                                                                        │
│                                                                                                                 │
│    d. `orders` table:                                                                                           │
│       - Index on `delivery_window_id`, `delivery_zone_id`, and `delivery_type` columns for order management and │
│ reporting.                                                                                                      │
│                                                                                                                 │
│ 4. Constraints:                                                                                                 │
│                                                                                                                 │
│    a. `delivery_windows` table:                                                                                 │
│       - Primary Key constraint on `window_id` column.                                                           │
│       - Unique constraint on `zone_id`, `date`, and `time_slot_code` columns to ensure unique time slot         │
│ availability per zone and date.                                                                                 │
│       - Check constraint on `start_time` and `end_time` columns to ensure valid time slot definitions.          │
│       - Check constraint on `available_capacity` column to ensure it does not exceed the `base_capacity`.       │
│                                                                                                                 │
│    b. `delivery_zones` table:                                                                                   │
│       - Primary Key constraint on `zone_id` column.                                                             │
│       - Unique constraint on `zone_code` column to ensure unique zone identifiers.                              │
│       - Check constraint on `postal_code_pattern` column to ensure valid regular expression format.             │
│                                                                                                                 │
│    c. `lsp_capacity` table:                                                                                     │
│       - Primary Key constraint on `capacity_id` column.                                                         │
│       - Foreign Key constraints on `zone_id`, `window_id`, and `lsp_id` columns referencing the respective      │
│ tables.                                                                                                         │
│       - Check constraint on `total_capacity` and `reserved_capacity` columns to ensure valid capacity values.   │
│                                                                                                                 │
│    d. `orders` table:                                                                                           │
│       - Foreign Key constraints on `delivery_window_id` and `delivery_zone_id` columns referencing the          │
│ respective tables.                                                                                              │
│       - Check constraint on `delivery_type` column to ensure valid delivery types (STANDARD, EXPRESS,           │
│ SAME_DAY).                                                                                                      │
│                                                                                                                 │
│ The proposed changes to the physical data model aim to maintain data consistency, ensure backward               │
│ compatibility, follow data governance standards, and preserve data lineage. The new tables and table updates    │
│ provide the necessary infrastructure to support the same-day delivery service, including delivery window        │
│ management, zone-based coverage, and real-time LSP capacity tracking.                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                Execution Metrics                 
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric            ┃ Value                      ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ input_tokens      │ 1868                       │
│ output_tokens     │ 1066                       │
│ total_tokens      │ 2934                       │
│ execution_time    │ 10.859942                  │
│ active_objectives │ ['PDM_ANALYSIS']           │
│ timestamp         │ 2025-01-15T17:05:42.492893 │
