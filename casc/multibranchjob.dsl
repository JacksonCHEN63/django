multibranchPipelineJob('Multibranch_casc') {
    branchSources {
        github {
            remote('https://github.com/JacksonCHEN63/Django.git')
            repository('Django')
        }
    }
}
