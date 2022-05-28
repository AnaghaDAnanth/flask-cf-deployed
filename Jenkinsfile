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
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'anagha-creds', usernameVariable: 'AnaghaDAnanth', passwordVariable: 'devops9931']]) {
                    bat('git push https://${AnaghaDAnanth}:${devops9931}@github.com/AnaghaDAnanth/flask-cf-deployed.git  --tags -f --no-verify')
                }
            }
        }
    }
}
