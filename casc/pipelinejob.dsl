pipelineJob('Configuration as Code Plugin') {
    definition {
        cps {
            script('''
properties([parameters([booleanParam(defaultValue: false, description: '', name: 'isRelease')])])

node {

    stage("checkout") {
        echo "hello"
    } 
}            
            ''')
        }
    }
}
