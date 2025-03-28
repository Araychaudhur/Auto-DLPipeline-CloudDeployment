from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Model Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(Self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\n ------------------ ")
    
    except Exception as e:
        logger.exception(e)
        raise e