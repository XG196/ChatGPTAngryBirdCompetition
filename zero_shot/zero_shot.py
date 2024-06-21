from pathlib import Path

from chatgpt4pcg.competition import chat_with_chatgpt, run_evaluation
from chatgpt4pcg.models.trial_context import TrialContext
from chatgpt4pcg.models.trial_loop import TrialLoop
from dotenv import load_dotenv

### My imports
from openai import OpenAI
from dotenv import dotenv_values


class ZeroShotPrompting(TrialLoop):
    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        """
        Runs the zero-shot prompting.
        :param ctx: The trial context.
        :param target_character: The target character.
        :return: The generated text.
        """
        # prompt_template = open(Path("prompts/zero_shot.txt"), "r").read()
        prompt_template = open(Path(".\prompts\zero_shot.txt"), "r").read()
        response = chat_with_chatgpt(ctx, [{"role": "user", "content": prompt_template
                                     .replace("<OBJECT>", target_character)}])
        response = response[0]
        return response


if __name__ == "__main__":
    
    load_dotenv()
    
    ## pass the test
    #config = dotenv_values("..\.env")
    # print(config)
    # client = OpenAI(
    #     api_key=config['OPENAI_API_KEY'],
    # )

    ## pass the test
    # load_dotenv()
    # client = OpenAI()

    run_evaluation("zero_shot", ZeroShotPrompting, num_trials=10, characters=["I"])
