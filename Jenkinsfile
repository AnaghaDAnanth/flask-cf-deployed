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

        stage('SonarQube analysis') {
        steps{
        withSonarQubeEnv('sonarqube-8.9') { 
        // If you have configured more than one global server connection, you can specify its name
//      bat("${scannerHome}/bin/sonar-scanner")
        bat("mvn sonar:sonar")
        }
        }
        }
    }
}
