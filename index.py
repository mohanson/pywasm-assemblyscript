import pywasm


def env_abort(_: pywasm.Ctx):
    return


vm = pywasm.load('./build/optimized.wasm', {
    'env': {
        'abort': env_abort,
    }
})
r = vm.exec('add', [10, 20])
print(r)
