from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(debug=True,port=3000)