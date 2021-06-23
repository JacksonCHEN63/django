pipelineJob('Configuration as Code Plugin') {
    definition {
        cps {
            script('''
properties([parameters([booleanParam(defaultValue: false, description: '', name: 'isRelease')])])

agent any {

    stage("checkout") {
        echo "hello"
    } 
}            
            ''')
        }
    }
}
