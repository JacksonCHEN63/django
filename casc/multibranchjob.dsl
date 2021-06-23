multibranchPipelineJob('Multibranch_casc') {
    branchSources {
        git {
            remote('https://github.com/JacksonCHEN63/Django.git')
        }
    }
}
