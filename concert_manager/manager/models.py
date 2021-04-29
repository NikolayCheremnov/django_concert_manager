from django.db import models


class NonProgrammableConfiguration(models.Model):
    main_sample = models.CharField(max_length=200)
    sub_sample = models.CharField(max_length=200)
    left_sample = models.CharField(max_length=200)
    split = models.CharField(max_length=200)
    octave_upper = models.IntegerField()
    octave_lower = models.IntegerField()
    transpose = models.IntegerField()
    other = models.CharField(max_length=200)

    def __str__(self):
        return str(self.other)

    class Meta:
        verbose_name = 'Non Programmable Configuration'
        verbose_name_plural = 'Non Programmable Configurations'


class ProgrammableConfiguration(models.Model):
    header = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.header)

    class Meta:
        verbose_name = 'Programmable Configuration'
        verbose_name_plural = 'Programmable Configurations'


class Song(models.Model):
    header = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    programmable_configuration = models.ForeignKey(ProgrammableConfiguration, on_delete=models.CASCADE, null=True, blank=True)
    non_programmable_configuration = models.ForeignKey(NonProgrammableConfiguration, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.header)

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'


class LiveSet(models.Model):
    header = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.header)

    class Meta:
        verbose_name = 'Live Set'
        verbose_name_plural = 'Live Sets'


class SongSet(models.Model):
    number_in_set = models.IntegerField(unique=True)
    live_set = models.ForeignKey(LiveSet, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number_in_set)

    class Meta:
        verbose_name = 'Song Set'
        verbose_name_plural = 'Songs Sets'


class Concert(models.Model):
    header = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.header)

    class Meta:
        verbose_name = 'Concert'
        verbose_name_plural = 'Concerts'


class ConcertLiveSet(models.Model):
    number_in_concert = models.IntegerField(unique=True)
    live_set = models.ForeignKey(LiveSet, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number_in_concert)

    class Meta:
        verbose_name = 'Concert Live Set'
        verbose_name_plural = 'Concert Live Sets'
