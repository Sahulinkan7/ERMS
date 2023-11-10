pipeline{
    agent any
    environment {
        CRED_PASS = credentials('example-credentials-id')
    }
    stages
    {
        stage ("clone ERMS project code from github")
        {
            steps{
                echo "cloning from github repo"
                git url:"https://github.com/Sahulinkan7/ERMS.git",branch:"main"
            }
            post{
                success{
                    echo "github clone done"
                }
                failure{
                    echo "cloning failed"
                }
                
            }
        }
        stage (" Building the code : Building docker image ")
        {
            steps{
                echo "building docker image"
                sh "docker build -t erms ."
            }
            post{
                success{
                    echo "docker image building done."
                }
                failure{
                    echo "building docker image failed"
                }
            }
        }
        stage ("pushing image to docker hub ")
        {
            steps{
                echo "pushing image to dockerhub"
                withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubpass",usernameVariable:"dockerHubuser")]){
                    sh "docker tag erms ${env.dockerHubuser}/erms:latest"
                    // sh "docker login -u ${env.dockerHubuser} -p ${env.dockerHubpass}"
                    sh("docker login -u $CRED_PASS_USR:$CRED_PASS_PSW")
                    sh "docker push ${env.dockerHubuser}/erms:latest"
                }
                post{
                    success{
                        echo "image pushed to docker hub registry."
                    }
                    failure{
                        echo "error : image could not pushed to docker hub registry."
                    }
                }
            }
        }
        stage ("pulling and running docker image in slave node")
        {
            agent{
                label 'slave'
            }
            steps{
                echo "running docker image in aws slave node "
                sh "docker run -d -p 8000:8000 sahulinkan7/erms:latest"
            }
            post{
                success{
                    echo "********** container running successfully **********"
                }
                failure{
                    echo "************* docker container not running ***********"
                }
            }
        }
        
    }
    post{
        success{
            echo " ******************  pipeline executed successfully ***********************"
        }
        failure{
            echo " %%%%%%%%%%%%%%%  pipeline execution failed %%%%%%%%%%%%%%%%%%%"
        }
    }
}