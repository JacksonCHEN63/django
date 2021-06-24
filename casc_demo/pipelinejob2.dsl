pipelineJob('demo/pipelinejob2_casc') {
    definition {
        cps {
            script('''
node ("jackson") {
    stage("checkout") {
        echo "hiiiiiiiii"
    } 
}            
            ''')
            sandbox()
        }
    }
}
