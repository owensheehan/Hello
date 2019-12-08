pipeline {
    options {
        skipStagesAfterUnstable()
    }
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile HelloPython.py' 
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                 sh """
                python test.py -v -rs integration_test
                echo 'Testing'
                """
            }
            
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python HelloPython.py'
               
            }
            post {
                success {
                    archiveArtifacts 'HelloPython.py'
                }
            }
        }
    }
}
