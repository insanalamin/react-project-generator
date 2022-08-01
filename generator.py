import os
from os.path import join
from os import listdir, rmdir
from shutil import move
from typing import List


def touch(file_route: str, content: List[str]=[], write_method: str="w"):
        """Create or append file from array content

        Args:
            file_route (str): File path
            content (str): List of content line
            write_method (str): w for write a new file, a for append to existing file
        """

        print("touch", file_route)
        f = open(file_route, write_method)
        f.writelines(content)
        f.close()


def mkdir(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def remove_file_if_exist(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(file_path, "file not exist")

def init_index_tsx():

    touch("./src/index.tsx", list(map(
        lambda x: "{}\n".format(x),
        [
            "import { createRoot } from 'react-dom/client'",
            "import './index.css'",
            "import App from './App'",
            "import * as serviceWorkerRegistration from './serviceWorkerRegistration'",
            "import reportWebVitals from './reportWebVitals'",
            "",
            "const rootElement = document.getElementById('root')",
            "",
            "if(rootElement !== null) {",
            "  const root = createRoot(rootElement)",
            "  root.render(",
            "    <App />",
            "  )",
            "}",
            "",
            "serviceWorkerRegistration.unregister()",
            "",
            "reportWebVitals()",
        ])))


def init_default_theme_ts():

    touch("./src/shared/styles/default-theme.ts", list(map(
        lambda x: "{}\n".format(x),
        [
            "import { createTheme } from '@mui/material/styles'",
            "",
            "export const themeColors = [",
            "  '#f6bb00',",
            "  '#00aa90',",
            "  '#007d3c',",
            "  '#0094bb',",
            "  '#da251d',",
            "  '#551d35',",
            "  '#6be3d1',",
            "  '#005245',",
            "]",
            "",
            "const styles = {",
            "  color: {",
            "    main: '#1a505a',",
            "    dark: '#013d48',",
            "    text: 'rgb(41, 41, 41)',",
            "    border: {",
            "      light: 'rgba(41, 41, 41, 0.1)',",
            "    },",
            "  },",
            "  boxShadow: {",
            "    elevation1: `0 0 13px 0 rgba(58, 96, 106, 0.13)`,",
            "    elevation4: `0 0 18px 0 rgba(58, 96, 106, 0.55)`,",
            "  },",
            "}",
            "",
            "const defaultTheme = createTheme({",
            "  palette: {",
            "    primary: {",
            "      main: styles.color.main,",
            "      dark: styles.color.dark,",
            "    },",
            "  },",
            "  components: {",
            "    MuiPaper: {",
            "      styleOverrides: {",
            "        root: {",
            "        },",
            "        elevation1: {",
            "          boxShadow: styles.boxShadow.elevation1,",
            "        },",
            "        elevation4: {",
            "          boxShadow: styles.boxShadow.elevation4,",
            "        },",
            "      },",
            "    },",
            "    MuiCardHeader: {",
            "      styleOverrides: {",
            "        root: {",
            "          borderBottom: `1px solid ${styles.color.border.light}`,",
            "        },",
            "        content: {",
            "          '& .MuiTypography-h5': {",
            "            fontSize: '1rem',",
            "            fontWeight: 'bold',",
            "          },",
            "        },",
            "      },",
            "    },",
            "    MuiBreadcrumbs: {",
            "      styleOverrides: {",
            "        li: {",
            "          fontSize: '0.8125rem',",
            "          '& >a': {",
            "            color: styles.color.main,",
            "            textDecoration: 'none',",
            "          },",
            "          '& >p': {",
            "            fontSize: '0.8125rem',",
            "          },",
            "        },",
            "        separator: {",
            "          fontSize: '0.8125rem',",
            "        },",
            "      },",
            "    },",
            "  },",
            "})",
            "",
            "export {styles}",
            "export default defaultTheme",
        ])))


def init_app_tsx():

    touch("./src/App.tsx", list(map(
        lambda x: "{}\n".format(x),
        [
            "import {ThemeProvider} from '@mui/material/styles'",
            "import defaultTheme from './shared/styles/default-theme'",
            "import { HashRouter, Route, Routes, } from 'react-router-dom'",
            "import { CssBaseline } from '@mui/material'",
            "import { Home } from './modules/app/Home'",
            "",
            "const App = () => {",
            "  return (",
            "    <ThemeProvider theme={defaultTheme}>",
            "      <HashRouter>",
            "        <CssBaseline />",
            "        <Routes>",
            "          <Route index element={<Home />} />",
            "        </Routes>",
            "      </HashRouter>",
            "    </ThemeProvider>",
            "  )",
            "}",
            "",
            "export default App",
        ])))


def add_component(component_folder, component_file, component_class_name, url=None):

    print(component_folder, component_file)

    mkdir(component_folder)

    touch(component_file, list(map(
        lambda x: "{}\n".format(x),
        [
            "import { Grid } from '@mui/material'",
            "import { CommonWrapper } from '../../../../shared/components/wrapper/CommonWrapper'",
            "export const {} = () => {{".format(component_class_name),
            "  return (",
            "    <CommonWrapper>",
            "      <Grid container>",
            "        <Grid item>",
            "          {}".format(component_class_name),
            "        </Grid>",
            "      </Grid>",
            "    </CommonWrapper>",
            "  )",
            "}",
            "",
        ])))


def add_module_component(component_path, url=None):

    component_folder = "./src/modules/{}".format(component_path)
    component_file = "{}/index.tsx".format(component_folder)
    component_class_name = component_path.split("/")[-1]

    add_component(component_folder, component_file, component_class_name)

    
def add_shared_component(component_path, url=None):

    component_folder = "./src/shared/components/{}".format(component_path)
    component_file = "{}/index.tsx".format(component_folder)
    component_class_name = component_path.split("/")[-1]

    add_component(component_folder, component_file, component_class_name)


def generate_react_project():

    if not os.path.isdir("./project") and not os.path.isfile("package.json"):
        os.system('yarn create react-app project --template cra-template-pwa-typescript')

    if os.path.isdir("./project") and not os.path.isfile("package.json"):
        root = ''
        for filename in listdir(join(root, 'project')):
            move(join(root, 'project', filename), join(root, filename))
        rmdir(root)
        os.rmdir('./project')

    os.system('yarn add @mui/material @emotion/react @emotion/styled react-router-dom@6 axios geojson @types/geojson jotai ol @types/ol react-icons @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome')

    for file_path in ['./src/logo.svg', './src/App.css']:
        remove_file_if_exist(file_path)

    for folder_path in [
        './src/shared/types',
        './src/shared/styles',
        './src/shared/components',
    ]:
        mkdir(folder_path)

    init_default_theme_ts()
    init_index_tsx()
    init_app_tsx()
    add_module_component("app/Home")

# generate_react_project()
# add_module_component("animals/Ant")
