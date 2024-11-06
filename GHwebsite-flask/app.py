from flask import Flask, render_template
from flask import Flask, request, jsonify, render_template
import requests
import psycopg2
# from opencensus.ext.azure.log_exporter import AzureLogHandler
# from opencensus.ext.azure.trace_exporter import AzureExporter
# from opencensus.trace.samplers import ProbabilitySampler
# from opencensus.trace.tracer import Tracer
# from opencensus.ext.flask.flask_middleware import FlaskMiddleware
#static folder path
app = Flask(__name__, static_folder='/home/website/GHwebsite/GHwebsite-flask/static')

# Database connection settings
DB_HOST = '172.188.42.27'
DB_NAME = 'dev'
DB_USER = 'odoo'
DB_PASSWORD = 'odoo'
DB_PORT = 9832

# Establishing the database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Database connected successfully")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Database connection failed: {e}")
        raise

# Instrumentation Key from Application Insights
instrumentation_key = '61b0aded-11b2-4181-ab29-fbe0c44763fd'

# # Configure Flask with Application Insights logging
# handler = AzureLogHandler(connection_string=f'InstrumentationKey={instrumentation_key}')
# exporter = AzureExporter(connection_string=f'InstrumentationKey={instrumentation_key}')
# tracer = Tracer(exporter=exporter, sampler=ProbabilitySampler(1.0))

# # Add Flask middleware to trace requests
# middleware = FlaskMiddleware(app, exporter=exporter, sampler=ProbabilitySampler(1.0))

# # Your Application Insights details
# application_id = 'b58890e2-d505-4961-b090-e31912ff8dc9'
# api_key = 'avgm1bywhmiy5be8nayndbzhkaul0pubjnlbupu2'

# # Azure Application Insights endpoint
# endpoint = f'https://api.applicationinsights.io/v1/apps/{application_id}/query'

# def get_analytics_data(query):
#     headers = {'x-api-key': api_key}
#     response = requests.get(endpoint, headers=headers, params={'query': query})
#     return response.json()

# @app.before_request
# def log_visitor_ip():
#     visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
#     span = tracer.span()  # Get the current span
#     span.add_annotation("Visitor IP logged")  # Add an annotation
#     span.add_attribute("Visitor IP", visitor_ip)  # Add IP address as an attribute


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/dashboard')
# def dashboard():
#     # Queries for summary and visitor data
#     query = """
#     requests
#     | where timestamp >= ago(7d)
#     | summarize total_requests = count(), unique_ips = dcount(client_IP), page_views = countif(itemType == "pageView")
#     """
#     summary_result = get_analytics_data(query)

#     region_query = """
#     requests
#     | where timestamp >= ago(7d)
#     | summarize visitor_count = count() by client_CountryOrRegion
#     | order by visitor_count desc
#     """
#     region_result = get_analytics_data(region_query)

#     ip_query = """
#     requests
#     | where timestamp >= ago(7d)
#     | summarize request_count = count() by client_IP
#     | order by request_count desc
#     """
#     ip_result = get_analytics_data(ip_query)

#     # Extracting data for the dashboard
#     total_visitors = summary_result['tables'][0]['rows'][0][0]
#     unique_ips = summary_result['tables'][0]['rows'][0][1]
#     page_views = summary_result['tables'][0]['rows'][0][2]

#     region_data = [(row[0], row[1]) for row in region_result['tables'][0]['rows']]
#     ip_data = [(row[0], row[1]) for row in ip_result['tables'][0]['rows']]

#     return render_template('dashboard.html',
#                            total_visitors=total_visitors,
#                            unique_ips=unique_ips,
#                            page_views=page_views,
#                            region_data=region_data,
#                            ip_data=ip_data)


@app.route('/home')
def home():
    return render_template('index.html')

# API endpoint to handle form submission
@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    try:
        # Get data from the request
        data = request.json

        # Extract form fields
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        company = data.get('company')
        subject = data.get('subject')
        message = data.get('message')

        # Validate input data (can be extended with more checks)
        if not all([name, email, phone, company, subject, message]):
            return jsonify({"error": "Missing required fields"}), 400

        # Insert data into the database
        query = """
        INSERT INTO crm_lead_form (contact_name, email, mobile, company_ids, lead_id, street)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (name, email, phone, company, subject, message)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, values)
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Form submitted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/business_area')
def business_area():
    return render_template('business_area.html')

@app.route('/article')
def article():
    return render_template('article.html')

@app.route('/direct_sales')
def direct_sales():
    return render_template('direct_sales.html')

@app.route('/retail_management')
def retail_management():
    return render_template('retail_management.html')

@app.route('/field_force_management')
def field_force_management():
    return render_template('field_force_management.html')

@app.route('/service_management')
def service_management():
    return render_template('service_management.html')

@app.route('/project_management')
def project_management():
    return render_template('project_management.html')

@app.route('/knowledge_management')
def knowledge_management():
    return render_template('knowledge_management.html')

@app.route('/manufacturing_management')
def manufacturing_management():
    return render_template('manufacturing_management.html')

@app.route('/inventory_management')
def inventory_management():
    return render_template('inventory_management.html')

@app.route('/hr_management')
def hr_management():
    return render_template('hr_management.html')

@app.route('/E_learning')
def e_learning():
    return render_template('E_learning.html')

@app.route('/multi_level_marketing')
def multi_level_marketing():
    return render_template('multi_level_marketing.html')

@app.route('/careers')
def carrers():
    return render_template('carrers.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/sector_manufacturing')
def sector_manufacturing():
    return render_template('sector_manufacturing.html')

@app.route('/sector_telecom')
def sector_telecom():
    return render_template('sector_telecom.html')

@app.route('/sector_pharma')
def sector_pharma():
    return render_template('sector_pharma.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/automotive')
def automotive():
    return render_template('automotive.html')

@app.route('/sectorRetail')
def sectorRetail():
    return render_template('sectorRetail.html')


if __name__ == '__main__':
    app.run(debug=True,port=8000)
