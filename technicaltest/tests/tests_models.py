from django.test import TestCase
from technicaltest.models import Home, MetaData


class HomeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Home.objects.create(display_text = 'MYOB Display Text')

    @classmethod
    def get_object(cls):
        return Home.objects.get(id=1)

    def test_display_text_label(self):
        self.assertEquals(HomeModelTest.get_object()._meta.get_field('display_text').verbose_name, 'display text')

    def test_display_text_value(self):
        self.assertEquals(HomeModelTest.get_object().display_text, 'MYOB Display Text')

    def test_display_text_max_length(self):
        self.assertEquals(HomeModelTest.get_object()._meta.get_field('display_text').max_length, 200)

    def test_object_name_is_display_text(self):
        self.assertEquals(f'{HomeModelTest.get_object().display_text}', str(HomeModelTest.get_object()))


class MetaDataModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods
        MetaData.objects.create(version = '0.0', description = 'MYOB Web App',
            last_commit_sha = 'abcd4312', commit_message = 'Source code changed')

    @classmethod
    def get_object(cls):
        return MetaData.objects.get(id=1)

    # Test 'version'
    def test_version_label(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('version').verbose_name, 'version')

    def test_version_value(self):
        self.assertEquals(MetaDataModelTest.get_object().version, '0.0')

    def test_display_text_max_length(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('version').max_length, 10)

    def test_object_name_is_version_comma_description(self):
        expected_object_name = f'{MetaDataModelTest.get_object().version}, {MetaDataModelTest.get_object().description}'
        self.assertEquals(expected_object_name, str(MetaDataModelTest.get_object()))

    # Test 'description'
    def test_description_label(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('description').verbose_name, 'description')

    def test_description_value(self):
        self.assertEquals(MetaDataModelTest.get_object().description, 'MYOB Web App')

    # Test 'last_commit_sha'
    def test_last_commit_sha_label(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('last_commit_sha').verbose_name, 'last commit sha')

    def test_last_commit_sha_value(self):
        self.assertEquals(MetaDataModelTest.get_object().last_commit_sha, 'abcd4312')

    def test_last_commit_sha_max_length(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('last_commit_sha').max_length, 50)

    def test_last_commit_sha_blank(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('last_commit_sha').blank, True)

    # Test 'commit_message'
    def test_commit_message_label(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('commit_message').verbose_name, 'commit message')

    def test_commit_message_value(self):
        self.assertEquals(MetaDataModelTest.get_object().commit_message, 'Source code changed')

    def test_commit_message_max_length(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('commit_message').max_length, 200)

    def test_commit_message_default(self):
        self.assertEquals(MetaDataModelTest.get_object()._meta.get_field('commit_message').default, 'Code Commit')
