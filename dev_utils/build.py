import os.path
import pathlib
import platform
import subprocess
import time

from dev_utils import clear


def build(withconsole, path, filedict, companyname, product_version, icon):
    try:
        system = platform.system()

        if system == "Windows":
            clear.code_foromat_and_make_requirements_txt(path=os.path.dirname(path))
            buildfile_name = path
            Output_dir_name = os.path.join(
                os.path.dirname(path), f"{pathlib.Path(path).stem}_build"
            )
            print(buildfile_name, Output_dir_name)

            should_include = []
            for i in range(0, len(filedict)):
                should_include.append(os.path.join(os.path.dirname(path), filedict[i]))

            print(should_include)
            if withconsole:
                if icon is None:
                    command = (
                        f"python -m nuitka --mingw64 --show-modules --follow-imports "
                        f"--windows-company-name={companyname} --windows-product-version={product_version} "
                        f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
                        f"--include-package=pygame "
                    )
                    for i in range(0, len(should_include)):
                        command += (
                            f"--include-data-dir={should_include[i]}={filedict[i]} "
                        )
                    command += f"{buildfile_name}"
                else:
                    command = (
                        f"python -m nuitka --mingw64 --show-modules --follow-imports "
                        f"--windows-company-name={companyname} --windows-product-version={product_version} "
                        f"--windows-icon-from-ico={icon} "
                        f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
                        f"--include-package=pygame "
                    )
                    for i in range(0, len(should_include)):
                        command += (
                            f"--include-data-dir={should_include[i]}={filedict[i]} "
                        )
                    command += f"{buildfile_name}"
            else:
                if icon is None:
                    command = (
                        f"python -m nuitka --mingw64 --show-modules --follow-imports "
                        f"--windows-company-name={companyname} --windows-product-version={product_version} "
                        f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
                        f"--windows-disable-console "
                        f"--include-package=pygame "
                    )
                    for i in range(0, len(should_include)):
                        command += (
                            f"--include-data-dir={should_include[i]}={filedict[i]} "
                        )
                    command += f"{buildfile_name}"
                else:
                    command = (
                        f"python -m nuitka --mingw64 --show-modules --follow-imports "
                        f"--windows-company-name={companyname} --windows-product-version={product_version} "
                        f"--windows-icon-from-ico={icon} "
                        f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
                        f"--windows-disable-console "
                        f"--include-package=pygame "
                    )
                    for i in range(0, len(should_include)):
                        command += (
                            f"--include-data-dir={should_include[i]}={filedict[i]} "
                        )
                    command += f"{buildfile_name}"

            print(command)
            start = time.time()
            subprocess.run(command.split(" "), shell=True, check=True)
            end = time.time()

            print(f"{end - start}s 사용됨")
            print(command)

        elif system == "Linux":
            clear.code_foromat_and_make_requirements_txt(path=os.path.dirname(path))
            buildfile_name = path
            Output_dir_name = os.path.join(
                os.path.dirname(path), f"{pathlib.Path(path).stem}_build"
            )
            print(buildfile_name, Output_dir_name)

            should_include = []
            for i in range(0, len(filedict)):
                should_include.append(os.path.join(os.path.dirname(path), filedict[i]))

            print(should_include)
            if withconsole:
                if icon is None:
                    command = (
                        f"python3 -m nuitka --mingw64 --show-modules --follow-imports "
                        f"--windows-company-name={companyname} --windows-product-version={product_version} "
                        f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
                        f"--include-package=pygame "
                    )
                    for i in range(0, len(should_include)):
                        command += (
                            f"--include-data-dir={should_include[i]}={filedict[i]} "
                        )
                    command += f"{buildfile_name}"
                else:
                    command = (
                        f"python3 -m nuitka --mingw64 --show-modules --follow-imports "
                        f"--windows-company-name={companyname} --windows-product-version={product_version} "
                        f"--windows-icon-from-ico={icon} "
                        f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
                        f"--include-package=pygame "
                    )
                    for i in range(0, len(should_include)):
                        command += (
                            f"--include-data-dir={should_include[i]}={filedict[i]} "
                        )
                    command += f"{buildfile_name}"
            else:
                if icon is None:
                    command = (
                        f"python3 -m nuitka --mingw64 --show-modules --follow-imports "
                        f"--windows-company-name={companyname} --windows-product-version={product_version} "
                        f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
                        f"--windows-disable-console "
                        f"--include-package=pygame "
                    )
                    for i in range(0, len(should_include)):
                        command += (
                            f"--include-data-dir={should_include[i]}={filedict[i]} "
                        )

                    command += f"{buildfile_name}"
                else:
                    command = (
                        f"python3 -m nuitka --mingw64 --show-modules --follow-imports "
                        f"--windows-company-name={companyname} --windows-product-version={product_version} "
                        f"--windows-icon-from-ico={icon} "
                        f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
                        f"--windows-disable-console "
                        f"--include-package=pygame "
                    )
                    for i in range(0, len(should_include)):
                        command += (
                            f"--include-data-dir={should_include[i]}={filedict[i]} "
                        )
                    command += f"{buildfile_name}"

            print(command)
            start = time.time()
            subprocess.run(command.split(" "), shell=True, check=True)
            end = time.time()

            print(f"{end - start}s 사용됨")
            print(command)
        elif system == "Darwin":
            print(system)
        else:
            print("OS를 알 수 없음")
    except Exception as e:
        print(e)
