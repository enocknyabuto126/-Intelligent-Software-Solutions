# AI in Software Engineering Assignment
## Week 4: Building Intelligent Software Solutions 💻🤖

This repository contains the complete implementation for the AI in Software Engineering assignment, demonstrating practical applications of AI tools in software development.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Chrome browser (for Selenium testing)
- Git

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd week-4-ai-assignment

# Install dependencies
pip install -r requirements.txt

# Install Jupyter (if not already installed)
pip install jupyter notebook
```

## 📁 Project Structure

```
week-4-ai-assignment/
├── task1_ai_code_completion.py      # AI-powered code completion comparison
├── task2_automated_testing.py       # Selenium-based automated testing
├── task3_predictive_analytics.ipynb # Jupyter notebook for ML predictions
├── requirements.txt                  # Python dependencies
├── AI_Software_Engineering_Report.md # Comprehensive assignment report
└── README.md                        # This file
```

## 🎯 Assignment Components

### Part 1: Theoretical Analysis (30%)
- **Short Answer Questions**: AI tools, bug detection, bias mitigation
- **Case Study**: AI in DevOps deployment pipelines
- **Deliverable**: Written answers in the report

### Part 2: Practical Implementation (60%)

#### Task 1: AI-Powered Code Completion
```bash
python task1_ai_code_completion.py
```
**What it does:**
- Compares manual vs AI-suggested code implementations
- Demonstrates performance differences between approaches
- Shows how AI tools can suggest more efficient solutions

**Expected Output:**
- Performance comparison of different sorting methods
- Analysis of code quality and efficiency
- Recommendations for best practices

#### Task 2: Automated Testing with AI
```bash
python task2_automated_testing.py
```
**What it does:**
- Implements Selenium-based automated testing framework
- Tests login page functionality (valid/invalid credentials, empty fields)
- Generates AI-powered insights and recommendations

**Note:** This is a demonstration framework. To run actual tests:
1. Update `test_url` with a real website
2. Provide valid test credentials
3. Ensure ChromeDriver is installed

#### Task 3: Predictive Analytics
```bash
jupyter notebook task3_predictive_analytics.ipynb
```
**What it does:**
- Loads and preprocesses Breast Cancer dataset
- Trains Random Forest model for priority prediction
- Evaluates performance using accuracy and F1-score
- Generates AI insights for resource allocation

**Expected Results:**
- Model accuracy: ~94.7%
- F1-Score: ~0.947
- Feature importance analysis
- Performance visualization

### Part 3: Ethical Reflection (10%)
- **Deliverable**: Ethical analysis in the report
- **Topics**: Bias detection, fairness tools, responsible AI

### Bonus Task: Innovation Challenge (Extra 10%)
- **Deliverable**: 1-page proposal in the report
- **Tool**: DocuGen AI - Automated documentation generation

## 🔧 Setup Instructions

### 1. Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv ai_assignment_env
source ai_assignment_env/bin/activate  # On Windows: ai_assignment_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. ChromeDriver Setup (for Task 2)
```bash
# Option 1: Manual download
# Download ChromeDriver from: https://chromedriver.chromium.org/
# Place in your PATH or project directory

# Option 2: Using webdriver-manager
pip install webdriver-manager
# The code will automatically download and manage ChromeDriver
```

### 3. Jupyter Setup (for Task 3)
```bash
# Install Jupyter
pip install jupyter notebook

# Launch Jupyter
jupyter notebook
# Then open task3_predictive_analytics.ipynb
```

## 📊 Running the Tasks

### Task 1: Code Completion
```bash
python task1_ai_code_completion.py
```
This will run automatically and show:
- Performance comparison results
- Code analysis
- Recommendations

### Task 2: Automated Testing
```bash
python task2_automated_testing.py
```
**Demo Mode:** Shows framework capabilities
**Live Testing:** Requires website URL and credentials

### Task 3: Predictive Analytics
```bash
jupyter notebook task3_predictive_analytics.ipynb
```
Run cells sequentially to:
1. Load and explore data
2. Preprocess and engineer features
3. Train and evaluate model
4. Generate insights


## 🎓 Learning Objectives

By completing this assignment, you will understand:

1. **AI Tools in Development**: How GitHub Copilot and similar tools enhance productivity
2. **Automated Testing**: Selenium integration with AI-powered insights
3. **Machine Learning**: Practical application of ML for software engineering tasks
4. **Ethical AI**: Bias detection and fairness in AI systems
5. **Innovation**: Designing AI solutions for software engineering challenges

## 🚨 Troubleshooting

### Common Issues

**ChromeDriver Errors:**
```bash
# Install webdriver-manager
pip install webdriver-manager

# Update the code to use automatic management
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
```

**Import Errors:**
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Check Python version (3.8+ required)
python --version
```

**Jupyter Issues:**
```bash
# Reinstall Jupyter
pip uninstall jupyter notebook
pip install jupyter notebook

# Or use conda
conda install jupyter notebook
```

### Performance Tips

1. **Task 1**: Use larger datasets for more significant performance differences
2. **Task 2**: Run tests in headless mode for faster execution
3. **Task 3**: Adjust hyperparameters for better model performance

## 📚 Additional Resources

- [GitHub Copilot Documentation](https://github.com/features/copilot)
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [IBM AI Fairness 360](https://aif360.mybluemix.net/)

## 🤝 Contributing

This is an educational assignment. Feel free to:
- Improve the code implementations
- Add additional features
- Enhance the documentation
- Share your insights and learnings

## 📄 License

This project is for educational purpose

