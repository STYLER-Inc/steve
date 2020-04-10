import pytest

from steve import load_yaml_file, \
        load_templates, \
        get_template_env


@pytest.fixture
def values():
    """ Loads values for the test template.
    """
    return load_yaml_file('tests/data/values.yaml')


@pytest.fixture
def template():
    """ Gets the template object for the test template.
    """
    template_dirs = ['tests/data']
    fs_loader = load_templates(template_dirs)
    template_env = get_template_env(fs_loader)
    return template_env.get_template('template.yaml')


class TestRenderTemplates:
    """ Tests rendering a template file with values.
    """
    def test_load_values(self, values):
        """ Tests loading test values.
        """
        expected_values = {
            'general': {
                'repo': 'asia.gcr.io/test-project'
            },
            'projects': {
                'test': {
                    'database': {
                        'ip': '1.2.3.4'
                    },
                    'name': 'test-service'
                }
            }
        }
        assert values == expected_values


    def test_template(self, values, template):
        """ Tests that template renders as expected.
        """
        expected_result_path = 'tests/data/expected-render-result.yaml'
        with open(expected_result_path, 'r') as expected_result:
            assert template.render(values) == expected_result.read()
