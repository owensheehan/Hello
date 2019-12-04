pipeline {
    
    agent any

    stages {
        stage('build') {
        
            steps {
                sh """
                python HelloPython.py
                echo 'Building'
                """
            }
        }
        stage('Test') {
            steps {
                sh """
                test.py -v -rs integration_test
                echo 'Testing'
                """
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}

