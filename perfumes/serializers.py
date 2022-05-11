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
            perfume_name=data["perfume_name"],
            notes=data['notes'],
            description=data['description'],
            price=data['price'],
            comment=data['comment'],
            perfume_image=data['perfume_image'],
        )

        if brand_data:
            brand, _created = Brand.objects.get_or_create(**brand_data)
            perfume.brand = brand

        # set the creator of a perfume to be the currently logged-in user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            perfume.creator = request.user

        # Need to save to get the id
        perfume.save()

        # render to the api
        return perfume

    def update(self, perfume, data):
        brand_data = data.pop("brand_name")

        perfume.perfume_name = data.get("perfume_name", perfume.perfume_name)
        perfume.notes = data.get("notes", perfume.notes)
        perfume.description = data.get("description", perfume.description)
        perfume.price = data.get["price", perfume.price]
        perfume.perfume_image = data.get["perfume_image",
                                         perfume.perfume_image]

        if brand_data:
            brand, _created = Brand.objects.get_or_create(**brand_data)
            perfume.brand = brand

        # save to the database
        perfume.save()

        # render to the api
        return perfume
