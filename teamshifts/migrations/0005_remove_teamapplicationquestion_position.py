from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("teamshifts", "0004_cfm_configurable_default_fields"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="teamapplicationquestion",
            options={
                "ordering": ["pk"],
                "verbose_name": "Application Question",
                "verbose_name_plural": "Application Questions",
            },
        ),
        migrations.RemoveField(
            model_name="teamapplicationquestion",
            name="position",
        ),
    ]
