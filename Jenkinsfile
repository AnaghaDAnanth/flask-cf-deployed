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
                    bat('git add .')
                    bat('git commit -m "Triggered Build through Jenkins"')
                    bat('git push https://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@github.com/AnaghaDAnanth/flask-cf-deployed.git HEAD:refs/heads/main --force')
                }
            }
        }
    }
}
