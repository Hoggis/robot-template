@Library ('skaler-jenkins-library@safety') _

pipeline {
    agent {
        node {
            // label 'windows'
            label 'ubuntu'
        }
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '100'))
        timestamps()
        gitLabConnection('gitlab.siilicloud.com')
        timeout(100)
    }
    parameters {
        choice(name: 'ROBOT_ENV', choices: ['prod', 'test'], description: 'Determines the configuration.')
        string(
            name: 'ROBOT_STAGES', defaultValue: '<ROBOT_STAGES>',
            description: 'The process stages to be run, separated with spaces.'
        )
    }
    environment {
        DB_CRED = credentials('demo-robo-mongo')
        JIRA_COMPONENT = '<MY_COMPONENT>'
    }

    stages {
        stage('Get source code') {
            steps {
                cleanWs()
                script {
                    buildUtils.getLastSuccesfulBuild(
                        "${JOB_BASE_NAME}-build/${miscUtils.getGitBranchName()}"
                    )
                }
            }
        }
        stage('Set up environment') {
            steps {
                script {
                    // bat "./scripts/start.cmd setup_env"
                    sh 'scripts/start.sh setup_env'
                }
            }
        }
        stage('Safety check') {
            steps {
                warnError(message: 'Safety found vulnerabilities in Python dependencies') {
                    script {
                        // bat "./scripts/start.cmd safety"
                        sh 'scripts/start.sh safety'
                    }
                }
            }
        }
        stage('Run process') {
            steps {
                script {
                    // bat "./scripts/start.cmd process"
                    sh 'scripts/start.sh process'
                }
            }
        }
    }
    post {
        always {
            script {
                robot(outputPath: 'output',
                      logFileName: 'log*.html',
                      outputFileName: 'output*.xml',
                      reportFileName: 'report*.html',
                      otherFiles: '**/*screenshot*.png'
                )
                if ( params.ROBOT_ENV == 'prod' ) {
                    analytics.pushBuildInformation(fields=null, env.JOB_BASE_NAME)
                }
            }
        }
        unsuccessful {
            script {
                if ( shouldEscalateFailure() ) {
                    jira.raiseIssue(
                        summary:"${JOB_BASE_NAME} failed! (#${currentBuild.id})",
                        description: readFile('output/errors.txt'),
                        component:env.JIRA_COMPONENT
                    )
                }
            }
        }
    }
}

Boolean shouldEscalateFailure() {
    return params.ROBOT_ENV == 'prod' && !miscUtils.buildTriggeredManually()
}