import luigi
import os

import pathlib


class GetRawData(luigi.Task):

    _folder_path = pathlib.Path("data/raw/")

    def requires(self):
        return CreateFolderStructure()

    def output(self):
        return luigi.LocalTarget(f"{self._folder_path}/global-wheat-detection.zip")

    def run(self):

        os.system(f"cd {self._folder_path} && "
                  f"kaggle competitions download -c global-wheat-detection && "
                  f"unzip global-wheat-detection.zip -d ./")
        return