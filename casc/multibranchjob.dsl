multibranchPipelineJob('Multibranch_casc') {
    branchSources {
        github {
            remote('https://github.com/JacksonCHEN63/Django.git')
            repository('Django')
        }
    }
    it / factory(class: "org.jenkinsci.plugins.workflow.multibranch.WorkflowBranchProjectFactory") << {
            // pipeline jobs will have their script path set to `pipelines/customPipeline.groovy`
            scriptPath("Jenkinsfile")
}
