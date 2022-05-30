pipeline {
//None parameter in the agent section means that no global agent will be allocated for the entire Pipeline’s
//execution and that each stage directive must specify its own agent section.
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python -m py_compile myapp.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        
        
        stage('Publish') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'anagha-creds', usernameVariable: 'AnaghaDAnanth', passwordVariable: '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']]) {                   
                    
                    bat('git push https://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@github.com/AnaghaDAnanth/flask-cf-deployed.git HEAD:refs/heads/main --tags -f --no-verify')
                }
            }
        }

        stage("Py Test") {
            steps{
                bat 'pip install --user -r requirements.txt'
                bat 'pip install -u pytest'
                bat 'py.test test_app.py'
            }
        }
        
        stage("Selenium Test") {
            steps{
                  bat 'python -m py_compile Selenium.py'
            }
            
             post {
        always {
        
            junit 'build/reports/**/*.xml'
        }
    }
        }

        stage('SonarQube analysis') {

        steps {
                script {
                    scannerHome = tool 'SonarqubeScanner-4.7';
                }
                withSonarQubeEnv('Sonarqube') {
                    bat "${scannerHome}/bin/sonar-scanner.bat" 
                }
            }
        }
    }
}

