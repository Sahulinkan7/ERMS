pipeline{
    agent any
    stages{
        stage ("clone ERMS project code from github"){
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
        stage (" Building the code : Building docker image "){
            steps{
                echo "building docker image"
                sh "docker build -t erms:latest ."
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
        
    }
}