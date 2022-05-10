from rest_framework import serializers
from brands.models import Brand
from perfumes.models import Perfume


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("brand_name",)


class PerfumeSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Perfume
        fields = '__all__'

    def create(self, data):
        brand_data = data.pop("brand")

        # perfume = perfume(**data)
        perfume = Perfume(
            title=data["title"],
            year_of_publication=data['year_of_publication'],
            rating=data['rating'],
            genre=data['genre'],
            language=data['language'],
        )

        if brand_data:
            brand, _created = Brand.objects.get_or_create(**brand_data)
            perfume.brand = brand

        # set the creator of a perfume to be the currently logged-in user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            perfume.createdBy = request.user

        # Need to save to get the id
        perfume.save()

        # render to the api
        return perfume

    def update(self, perfume, data):
        brand_data = data.pop("brand")

        perfume.title = data.get("title", perfume.title)
        perfume.rating = data.get("rating", perfume.rating)
        perfume.year_of_publication = data.get(
            "year_of_publication", perfume.year_of_publication)

        if brand_data:
            brand, _created = Brand.objects.get_or_create(**brand_data)
            perfume.brand = brand

        # save to the database
        perfume.save()

        # render to the api
        return perfume
