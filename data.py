# ---------------- DATA ---------------- #
job_data = {
    "Engineering / Tech": {
        "Software Development": ["Frontend Developer","Backend Developer","Full Stack Developer","Software Engineer"],
        "Data Science & Analytics": ["Data Analyst","Data Scientist","Business Intelligence Analyst","Analytics Engineer"],
        "Artificial Intelligence & Machine Learning": ["Machine Learning Engineer","AI Engineer","NLP Engineer","Computer Vision Engineer"],
        "Cloud Computing": ["Cloud Engineer","Cloud Architect","Solutions Architect"],
        "DevOps & Infrastructure": ["DevOps Engineer","Site Reliability Engineer (SRE)","Infrastructure Engineer"],
        "Cybersecurity": ["Security Engineer","Security Analyst","Ethical Hacker / Penetration Tester"],
        "Mobile Development": ["Android Developer","iOS Developer","Cross-platform Developer (Flutter/React Native)"],
        "Web Development": ["Web Developer","Frontend Engineer","Backend Engineer"]
    },

    "Product Team": {
        "Product Management": ["Product Manager","Associate Product Manager (APM)"],
        "Product Strategy": ["Product Strategist","Strategy Analyst"],
        "Product Analytics": ["Product Analyst","Data Analyst (Product)"],
        "Product Operations": ["Product Operations Manager","Program Manager"],
        "Technical Product Management": ["Technical Product Manager","Platform Product Manager"]
    },

    "Design Team": {
        "UI Design": ["UI Designer","Visual Interface Designer"],
        "UX Design": ["UX Designer","Interaction Designer"],
        "Product Design": ["Product Designer"],
        "UX Research": ["UX Researcher","User Research Analyst"],
        "Visual Design": ["Graphic Designer","Visual Designer"],
        "Motion / Animation Design": ["Motion Designer","Animator"]
    },

    "Marketing Team": {
        "Digital Marketing": ["Digital Marketing Specialist","Online Marketing Manager"],
        "Content Marketing": ["Content Writer","Content Strategist"],
        "Social Media Marketing": ["Social Media Manager","Social Media Executive"],
        "SEO": ["SEO Specialist","SEO Analyst"],
        "SEM": ["SEM Specialist","Paid Ads Specialist"],
        "Performance Marketing": ["Performance Marketer","Growth Analyst"],
        "Brand Marketing": ["Brand Manager","Brand Strategist"],
        "Growth Marketing": ["Growth Marketer","Growth Manager"]
    },

    "Sales Team": {
        "Business Development": ["Business Development Executive (BDE)","Business Development Manager (BDM)"],
        "B2B Sales": ["B2B Sales Executive","Enterprise Sales Manager"],
        "B2C Sales": ["Sales Executive","Retail Sales Associate"],
        "Inside Sales": ["Inside Sales Representative","Sales Development Representative (SDR)"],
        "Field Sales": ["Field Sales Executive","Territory Sales Manager"],
        "Account Management": ["Account Manager","Key Account Manager"],
        "Pre-Sales": ["Pre-Sales Consultant","Solutions Consultant"]
    },

    "Human Resources (HR)": {
        "Talent Acquisition / Recruitment": ["Recruiter","Talent Acquisition Specialist"],
        "Employee Relations": ["Employee Relations Specialist"],
        "Learning & Development (L&D)": ["L&D Specialist","Training Manager"],
        "Compensation & Benefits": ["Compensation Analyst","Benefits Specialist"],
        "HR Operations": ["HR Operations Executive","HR Coordinator"],
        "Organizational Development": ["Organizational Development Specialist","HR Business Partner (HRBP)"]
    },

    "Finance Team": {
        "Accounting": ["Accountant","Junior Accountant"],
        "Financial Planning & Analysis (FP&A)": ["Financial Analyst","FP&A Analyst"],
        "Auditing": ["Auditor","Internal Auditor"],
        "Taxation": ["Tax Analyst","Tax Consultant"],
        "Payroll": ["Payroll Specialist","Payroll Executive"],
        "Risk Management": ["Risk Analyst","Compliance Analyst"],
        "Investment / Treasury": ["Treasury Analyst","Investment Analyst"]
    },

    "Customer Support / Success": {
        "Customer Support": ["Customer Support Executive","Support Agent"],
        "Technical Support": ["Technical Support Engineer","IT Support Specialist"],
        "Customer Success": ["Customer Success Manager (CSM)","Customer Success Associate"],
        "Customer Experience (CX)": ["Customer Experience Specialist","CX Analyst"],
        "Client Onboarding": ["Onboarding Specialist","Implementation Specialist"],
        "Customer Retention": ["Retention Specialist","Customer Engagement Manager"]
    }
}

tech_suggestions = {

    # ----------------------- SOFTWARE DEVELOPMENT -------------------------#
    "Frontend Developer": ["HTML","CSS","JavaScript","TypeScript","React","Angular","Vue.js","Redux","Tailwind CSS","Bootstrap","Webpack","Vite","REST APIs","GraphQL","Responsive Design","Cross-Browser Compatibility","Git"],

    "Backend Developer": ["Python","Java","Node.js","C#","Go","Ruby","Django","Flask","Spring Boot","Express.js","REST APIs","GraphQL","Microservices","Authentication (JWT/OAuth)","SQL","NoSQL","Redis","Docker","Git"],

    "Full Stack Developer": ["HTML","CSS","JavaScript","TypeScript","React","Angular","Vue.js","Node.js","Express.js","Django","Flask","Spring Boot","REST APIs","GraphQL","SQL","MongoDB","Firebase","Docker","Git","CI/CD"],

    "Software Engineer": ["Data Structures","Algorithms","OOP","System Design","Operating Systems","Computer Networks","Databases","C++","Java","Python","Git","Linux","Debugging","Testing","Design Patterns"],


    # ---------------- DATA SCIENCE & ANALYTICS ---------------- #
    "Data Analyst": ["Python","Pandas","NumPy","SQL","Excel","Power BI","Tableau","Data Cleaning","Data Visualization","Statistics","A/B Testing","Reporting","ETL"],

    "Data Scientist": ["Python","Pandas","NumPy","Scikit-learn","TensorFlow","PyTorch","SQL","Statistics","Machine Learning","Deep Learning","Data Visualization","Feature Engineering","NLP","Model Evaluation"],

    "Business Intelligence Analyst": ["SQL","Power BI","Tableau","Excel","Data Warehousing","ETL","Data Modeling","Dashboarding","Reporting","Business Analysis"],

    "Analytics Engineer": ["SQL","dbt","Python","Data Modeling","ETL","Data Warehousing","Snowflake","BigQuery","Redshift","Airflow"],


    # ---------------- AI & ML ---------------- #
    "Machine Learning Engineer": ["Python","Scikit-learn","TensorFlow","PyTorch","ML Algorithms","Feature Engineering","Model Deployment","Docker","Kubernetes","CI/CD","API Development","MLOps"],

    "AI Engineer": ["Python","TensorFlow","PyTorch","Deep Learning","NLP","Computer Vision","Transformers","OpenAI APIs","LangChain","Model Deployment","MLOps"],

    "NLP Engineer": ["Python","NLTK","spaCy","Transformers","Hugging Face","BERT","GPT","Text Processing","Tokenization","Named Entity Recognition","Sentiment Analysis"],

    "Computer Vision Engineer": ["Python","OpenCV","TensorFlow","PyTorch","CNN","Object Detection","Image Processing","YOLO","Segmentation","Deep Learning"],


    # ---------------- CLOUD ---------------- #
    "Cloud Engineer": ["AWS","Azure","Google Cloud","Docker","Kubernetes","Terraform","CI/CD","Linux","Networking","Security","Monitoring"],

    "Cloud Architect": ["AWS","Azure","Google Cloud","System Design","Microservices","Networking","Security","Scalability","Terraform","Kubernetes","Cost Optimization"],

    "Solutions Architect": ["System Design","Cloud Platforms","APIs","Microservices","Networking","Security","Client Communication","Architecture Design"],


    # ---------------- DEVOPS ---------------- #
    "DevOps Engineer": ["Docker","Kubernetes","Jenkins","GitHub Actions","CI/CD","Terraform","Ansible","Linux","Monitoring","Prometheus","Grafana","AWS","Azure"],

    "Site Reliability Engineer (SRE)": ["Linux","Python","Go","Monitoring","Prometheus","Grafana","Incident Management","CI/CD","Kubernetes","Automation","Distributed Systems"],

    "Infrastructure Engineer": ["Linux","Networking","Cloud Platforms","Terraform","Ansible","Docker","Kubernetes","Security","System Administration"],


    # ---------------- CYBERSECURITY ---------------- #
    "Security Engineer": ["Network Security","Cryptography","Firewalls","SIEM","Penetration Testing","Vulnerability Assessment","Python","Linux","Security Tools"],

    "Security Analyst": ["SIEM","Threat Analysis","Incident Response","Network Monitoring","Firewalls","IDS/IPS","Log Analysis","Cyber Threat Intelligence"],

    "Ethical Hacker / Penetration Tester": ["Penetration Testing","Kali Linux","Metasploit","Burp Suite","Nmap","OWASP","Web Security","Exploitation","Scripting"],


    # ---------------- MOBILE ---------------- #
    "Android Developer": ["Java","Kotlin","Android SDK","Jetpack","Firebase","REST APIs","UI/UX","Material Design","Git"],

    "iOS Developer": ["Swift","Objective-C","iOS SDK","Xcode","UIKit","CoreData","REST APIs","Git"],

    "Cross-platform Developer (Flutter/React Native)": ["Dart","Flutter","React Native","JavaScript","TypeScript","REST APIs","Firebase","Mobile UI","Git"],


    # ---------------- WEB ---------------- #
    "Web Developer": ["HTML","CSS","JavaScript","React","Node.js","Express.js","MongoDB","REST APIs","Git","Responsive Design"],

    "Frontend Engineer": ["HTML","CSS","JavaScript","TypeScript","React","Next.js","Redux","Tailwind CSS","Performance Optimization","Accessibility","Testing"],

    "Backend Engineer": ["Python","Java","Node.js","Go","Django","Spring Boot","Express.js","Databases","REST APIs","Microservices","Docker","CI/CD"],

    # ---------------- PRODUCT MANAGEMENT ---------------- #
    "Product Manager": [
        "Product Lifecycle Management","Roadmapping","User Stories","Agile","Scrum",
        "Stakeholder Management","Market Research","User Research","Wireframing",
        "Figma","A/B Testing","Metrics (KPIs/OKRs)","Business Strategy",
        "Communication","Problem Solving","Data Analysis"
    ],

    "Associate Product Manager (APM)": [
        "Product Lifecycle Basics","Agile","Scrum","User Stories","Market Research",
        "User Research","Figma","Wireframing","SQL (Basic)","Data Analysis",
        "Communication","Problem Solving","Stakeholder Coordination"
    ],


    # ---------------- PRODUCT STRATEGY ---------------- #
    "Product Strategist": [
        "Market Analysis","Competitive Analysis","Business Strategy","Growth Strategy",
        "Product Positioning","Customer Segmentation","SWOT Analysis","OKRs",
        "Data Analysis","Financial Modeling","Communication","Decision Making"
    ],

    "Strategy Analyst": [
        "Data Analysis","Excel","SQL","Market Research","Business Analysis",
        "Financial Analysis","Forecasting","Reporting","Problem Solving",
        "Presentation Skills"
    ],


    # ---------------- PRODUCT ANALYTICS ---------------- #
    "Product Analyst": [
        "SQL","Python","Pandas","Data Visualization","Tableau","Power BI",
        "A/B Testing","Product Metrics","User Behavior Analysis",
        "Funnel Analysis","Cohort Analysis","Statistics","Experimentation"
    ],

    "Data Analyst (Product)": [
        "SQL","Python","Pandas","NumPy","Data Cleaning","Data Visualization",
        "Tableau","Power BI","Excel","Statistics","A/B Testing","Reporting"
    ],


    # ---------------- PRODUCT OPERATIONS ---------------- #
    "Product Operations Manager": [
        "Process Optimization","Product Lifecycle Management","Agile","Scrum",
        "Stakeholder Management","Project Management","Data Analysis",
        "Cross-functional Collaboration","Documentation","Communication",
        "Tooling (Jira, Confluence)"
    ],

    "Program Manager": [
        "Program Management","Project Management","Agile","Scrum","Risk Management",
        "Stakeholder Management","Planning","Execution","Communication",
        "Cross-functional Leadership","Time Management"
    ],


    # ---------------- TECHNICAL PRODUCT MANAGEMENT ---------------- #
    "Technical Product Manager": [
        "System Design","APIs","Microservices","Cloud (AWS/Azure/GCP)",
        "Software Development Basics","SQL","Data Analysis","Agile","Scrum",
        "Roadmapping","Technical Documentation","Stakeholder Management",
        "Communication"
    ],

    "Platform Product Manager": [
        "Platform Architecture","APIs","Microservices","Cloud Computing",
        "Scalability","System Design","Data Analysis","SQL","Agile","Scrum",
        "Stakeholder Management","Technical Strategy"
    ],

    # ---------------- UI DESIGN ---------------- #
    "UI Designer": [
        "Figma","Adobe XD","Sketch","Wireframing","Prototyping",
        "Visual Design","Typography","Color Theory","Design Systems",
        "Responsive Design","UI Components","Accessibility (WCAG)",
        "User Interface Principles"
    ],

    "Visual Interface Designer": [
        "Figma","Adobe XD","Sketch","Visual Design","Typography",
        "Color Theory","Layout Design","Design Systems",
        "Brand Consistency","Responsive Design","UI Patterns"
    ],


    # ---------------- UX DESIGN ---------------- #
    "UX Designer": [
        "User Research","Wireframing","Prototyping","Figma","Adobe XD",
        "User Flows","Information Architecture","Usability Testing",
        "Interaction Design","Accessibility","Design Thinking",
        "User-Centered Design"
    ],

    "Interaction Designer": [
        "Interaction Design","Prototyping","Figma","Adobe XD",
        "User Flows","Microinteractions","Usability Principles",
        "Human-Computer Interaction (HCI)","Animation Basics"
    ],


    # ---------------- PRODUCT DESIGN ---------------- #
    "Product Designer": [
        "Figma","Adobe XD","Sketch","Wireframing","Prototyping",
        "User Research","UX Design","UI Design","Design Systems",
        "Usability Testing","Interaction Design","Product Thinking",
        "Cross-functional Collaboration"
    ],


    # ---------------- UX RESEARCH ---------------- #
    "UX Researcher": [
        "User Research","Qualitative Research","Quantitative Research",
        "Surveys","Interviews","Usability Testing","A/B Testing",
        "Data Analysis","Behavior Analysis","Research Methods",
        "Persona Creation","Journey Mapping"
    ],

    "User Research Analyst": [
        "User Research","Data Analysis","Surveys","Interviews",
        "Usability Testing","A/B Testing","Statistics","Reporting",
        "Behavioral Analysis","Insights Generation"
    ],


    # ---------------- VISUAL DESIGN ---------------- #
    "Graphic Designer": [
        "Adobe Photoshop","Illustrator","InDesign",
        "Typography","Color Theory","Branding","Layout Design",
        "Creativity","Visual Storytelling","Print Design"
    ],

    "Visual Designer": [
        "Figma","Adobe Photoshop","Illustrator",
        "Typography","Color Theory","Branding","Layout Design",
        "Design Systems","UI Design","Visual Storytelling"
    ],


    # ---------------- MOTION / ANIMATION ---------------- #
    "Motion Designer": [
        "After Effects","Adobe Premiere Pro","Animation Principles",
        "Motion Graphics","Storyboarding","Video Editing",
        "2D Animation","Visual Effects","Creativity"
    ],

    "Animator": [
        "2D Animation","3D Animation","Blender","Maya",
        "Animation Principles","Rigging","Storyboarding",
        "Motion Graphics","Rendering","Creativity"
    ],

    # ---------------- MARKETING TEAM ---------------- #
    "Digital Marketing Specialist": [
        "SEO","SEM","Google Analytics","Social Media Marketing","Content Marketing",
        "Email Marketing","Google Ads","Facebook Ads","Campaign Management",
        "Conversion Optimization","Marketing Automation"
    ],

    "Online Marketing Manager": [
        "Digital Strategy","SEO","SEM","Analytics","Campaign Management",
        "Budgeting","Team Management","Performance Tracking","Marketing Tools"
    ],

    "Content Writer": [
        "Content Writing","SEO Writing","Copywriting","Blogging",
        "Research","Editing","Storytelling","Content Strategy"
    ],

    "Content Strategist": [
        "Content Planning","SEO","Audience Analysis","Content Marketing",
        "Editorial Calendar","Brand Voice","Analytics","Strategy"
    ],

    "Social Media Manager": [
        "Social Media Marketing","Content Creation","Analytics",
        "Campaign Management","Branding","Community Management",
        "Instagram","LinkedIn","Twitter"
    ],

    "Social Media Executive": [
        "Social Media","Content Creation","Scheduling Tools",
        "Engagement","Analytics","Basic Design"
    ],

    "SEO Specialist": [
        "SEO","Keyword Research","On-page SEO","Off-page SEO",
        "Technical SEO","Google Search Console","Analytics","Link Building"
    ],

    "SEO Analyst": [
        "SEO","Keyword Analysis","Google Analytics","Search Console",
        "Reporting","Competitor Analysis"
    ],

    "SEM Specialist": [
        "Google Ads","PPC","Keyword Bidding","Campaign Optimization",
        "Conversion Tracking","Analytics"
    ],

    "Paid Ads Specialist": [
        "Google Ads","Facebook Ads","PPC","Campaign Management",
        "Conversion Optimization","Analytics"
    ],

    "Performance Marketer": [
        "Performance Marketing","PPC","Analytics","A/B Testing",
        "Conversion Optimization","ROI Tracking"
    ],

    "Growth Analyst": [
        "Data Analysis","SQL","Excel","A/B Testing",
        "User Growth Metrics","Analytics","Experimentation"
    ],

    "Brand Manager": [
        "Brand Strategy","Marketing Campaigns","Market Research",
        "Communication","Positioning","Creative Direction"
    ],

    "Brand Strategist": [
        "Brand Strategy","Market Analysis","Customer Insights",
        "Positioning","Storytelling","Competitive Analysis"
    ],

    "Growth Marketer": [
        "Growth Hacking","A/B Testing","Analytics","SEO",
        "Email Marketing","Funnel Optimization"
    ],

    "Growth Manager": [
        "Growth Strategy","Analytics","Team Management",
        "Experimentation","Performance Tracking"
    ],


    # ---------------- SALES TEAM ---------------- #
    "Business Development Executive (BDE)": [
        "Lead Generation","Cold Calling","Sales Pitch","CRM Tools",
        "Communication","Negotiation","Prospecting"
    ],

    "Business Development Manager (BDM)": [
        "Business Strategy","Lead Generation","Negotiation",
        "Client Relationship","Sales Planning","Revenue Growth"
    ],

    "B2B Sales Executive": [
        "B2B Sales","Lead Generation","Negotiation","CRM",
        "Client Handling","Sales Funnel"
    ],

    "Enterprise Sales Manager": [
        "Enterprise Sales","Negotiation","Account Management",
        "Sales Strategy","Relationship Management"
    ],

    "Sales Executive": [
        "Sales","Customer Handling","Communication",
        "Negotiation","Product Knowledge"
    ],

    "Retail Sales Associate": [
        "Customer Service","Sales","Product Knowledge",
        "Communication","POS Systems"
    ],

    "Inside Sales Representative": [
        "Inside Sales","Cold Calling","CRM","Lead Qualification",
        "Communication","Sales Funnel"
    ],

    "Sales Development Representative (SDR)": [
        "Lead Generation","Cold Outreach","CRM",
        "Prospecting","Communication"
    ],

    "Field Sales Executive": [
        "Field Sales","Client Visits","Negotiation",
        "Territory Management","Sales Reporting"
    ],

    "Territory Sales Manager": [
        "Territory Management","Sales Strategy",
        "Team Handling","Revenue Tracking"
    ],

    "Account Manager": [
        "Account Management","Client Relationship",
        "Upselling","Communication","CRM"
    ],

    "Key Account Manager": [
        "Key Accounts","Relationship Management",
        "Negotiation","Strategic Planning"
    ],

    "Pre-Sales Consultant": [
        "Product Knowledge","Client Demos","Technical Understanding",
        "Solution Selling","Communication"
    ],

    "Solutions Consultant": [
        "Solution Design","Technical Knowledge","Client Interaction",
        "Presentation Skills","Problem Solving"
    ],


    # ---------------- HUMAN RESOURCES ---------------- #
    "Recruiter": [
        "Recruitment","Sourcing","Interviewing",
        "ATS Tools","Communication","Candidate Screening"
    ],

    "Talent Acquisition Specialist": [
        "Talent Acquisition","Sourcing","Employer Branding",
        "Interviewing","Hiring Strategy"
    ],

    "Employee Relations Specialist": [
        "Employee Engagement","Conflict Resolution",
        "Communication","HR Policies"
    ],

    "L&D Specialist": [
        "Training","Learning Programs","Content Creation",
        "Employee Development","Workshops"
    ],

    "Training Manager": [
        "Training Programs","Leadership","Curriculum Design",
        "Performance Tracking"
    ],

    "Compensation Analyst": [
        "Compensation","Salary Benchmarking",
        "Excel","Data Analysis"
    ],

    "Benefits Specialist": [
        "Employee Benefits","HR Policies",
        "Compliance","Communication"
    ],

    "HR Operations Executive": [
        "HR Operations","Payroll","HRMS",
        "Documentation","Compliance"
    ],

    "HR Coordinator": [
        "HR Support","Scheduling","Documentation",
        "Communication"
    ],

    "Organizational Development Specialist": [
        "Organizational Development","Change Management",
        "Employee Engagement","Strategy"
    ],

    "HR Business Partner (HRBP)": [
        "HR Strategy","Business Alignment",
        "Leadership","Employee Relations"
    ],


    # ---------------- FINANCE TEAM ---------------- #
    "Accountant": [
        "Accounting","Tally","Excel","Financial Statements",
        "Bookkeeping","GST"
    ],

    "Junior Accountant": [
        "Accounting Basics","Tally","Excel",
        "Bookkeeping"
    ],

    "Financial Analyst": [
        "Financial Analysis","Excel","Forecasting",
        "Modeling","Reporting"
    ],

    "FP&A Analyst": [
        "Financial Planning","Budgeting","Forecasting",
        "Excel","Data Analysis"
    ],

    "Auditor": [
        "Auditing","Compliance","Financial Statements",
        "Risk Assessment"
    ],

    "Internal Auditor": [
        "Internal Audits","Risk Management",
        "Compliance","Reporting"
    ],

    "Tax Analyst": [
        "Taxation","GST","Income Tax",
        "Compliance","Filing"
    ],

    "Tax Consultant": [
        "Tax Planning","GST","Income Tax",
        "Advisory"
    ],

    "Payroll Specialist": [
        "Payroll","HRMS","Compliance",
        "Salary Processing"
    ],

    "Payroll Executive": [
        "Payroll Processing","Excel",
        "HRMS"
    ],

    "Risk Analyst": [
        "Risk Analysis","Data Analysis",
        "Compliance","Reporting"
    ],

    "Compliance Analyst": [
        "Compliance","Regulations",
        "Auditing","Documentation"
    ],

    "Treasury Analyst": [
        "Treasury","Cash Flow","Investments",
        "Financial Analysis"
    ],

    "Investment Analyst": [
        "Investment Analysis","Market Research",
        "Financial Modeling","Valuation"
    ],


    # ---------------- CUSTOMER SUCCESS ---------------- #
    "Customer Support Executive": [
        "Customer Support","Communication",
        "Problem Solving","CRM Tools"
    ],

    "Support Agent": [
        "Customer Service","Ticketing Systems",
        "Communication","Issue Resolution"
    ],

    "Technical Support Engineer": [
        "Technical Support","Troubleshooting",
        "Networking Basics","OS Knowledge",
        "Communication"
    ],

    "IT Support Specialist": [
        "IT Support","Hardware","Software",
        "Networking","Troubleshooting"
    ],

    "Customer Success Manager (CSM)": [
        "Customer Success","Relationship Management",
        "Onboarding","Retention","Communication"
    ],

    "Customer Success Associate": [
        "Customer Support","Onboarding",
        "Communication","Retention"
    ],

    "Customer Experience Specialist": [
        "Customer Experience","Feedback Analysis",
        "Journey Mapping","Communication"
    ],

    "CX Analyst": [
        "Data Analysis","Customer Insights",
        "Reporting","Analytics"
    ],

    "Onboarding Specialist": [
        "Client Onboarding","Training",
        "Communication","Documentation"
    ],

    "Implementation Specialist": [
        "Implementation","Technical Setup",
        "Client Training","Troubleshooting"
    ],

    "Retention Specialist": [
        "Customer Retention","Engagement",
        "Communication","Analytics"
    ],

    "Customer Engagement Manager": [
        "Customer Engagement","Relationship Management",
        "Strategy","Communication"
    ]

}