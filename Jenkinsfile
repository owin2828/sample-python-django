pipeline {
    agent { label 'docker-python' }
    options {
        timestamps()
    }
    environment {
        PROJECT_NAME = "newdeal-python-sample"
    }
    stages {
        stage("dependency") {
            steps {
                //sh "pip install --user -r requirements.txt"
                 sh '''
                    pip install --user --trusted-host 10.217.65.18 \
                        -i http://devops.sw:'commonSW1234!'@10.217.65.18:8081/repository/pypi-sw-group/simple \
                        --timeout 60 \
                        -r requirements.txt
                    '''
            }
        }
         stage("Test"){
            steps{
                sh "python manage.py test"
            }
        }
        //stage("test") {
        //    steps {
        //        sh "echo pytest"
        //    }
        //}
        
        stage("Sonar") {
            steps {
                withSonarQubeEnv(installationName: 'SonarQube', credentialsId: 'newdeal-sonarqube') {
                    sh "sonar-scanner \
                      -Dsonar.projectKey=${PROJECT_NAME} "
                }
            }
        }
        
       
        
        stage("packaging") {
            steps {
                sh "python setup.py sdist bdist_wheel"
            }
        }
        stage("Deploy To Nexus") {
            steps {
                configFileProvider([configFile(fileId: 'sw_architecture_pypirc', targetLocation: '/home/jenkins/.pypirc')]) {
                    sh "twine upload ./dist/*"
                }
            }
        }
    }
}
