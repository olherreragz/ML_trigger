from Trigger import Trigger


if __name__ == "__main__":
    execution_layer = Trigger(json_path='algoparams_from_ui.json')

    "Trigger process"
    execution_layer.process.trigger_steps()
