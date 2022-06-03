pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        
        
        stage("Test") {
            steps{  
                bat 'pip install --default-timeout=100 regex'
                bat 'pip install --default-timeout=100 joblib'
                bat 'pip install --default-timeout=100 --user nltk'
                bat 'pip install flask'
                bat 'python -m pytest --junitxml results.xml test_routes.py'
            }
        }
        

        stage('Code Quality') {
            steps {
                    script {
                        scannerHome = tool 'SonarqubeScanner-4.7';
                    }
                    withSonarQubeEnv('Sonarqube') {
                        bat "${scannerHome}/bin/sonar-scanner.bat" 
                    }
                }
         }
        
        stage('Publish') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'anagha-creds', usernameVariable: 'AnaghaDAnanth', passwordVariable: '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']]) {                   
                    bat('git add .')
                    bat('git commit -m "Pushed from Jenkins - Build %BUILD_NUMBER%"')
                    bat('git push https://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@github.com/AnaghaDAnanth/flask-cf-deployed.git HEAD:refs/heads/test-deployment --tags -f --no-verify')
                }
            }
        }
    }
}

