from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import CreatePetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets,
    }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    # can_edit = pet.user == request.user
    # can_delete = pet.user == request.user
    is_owner = pet.user == request.user
    liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()

    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk
            }
        ),
        'comments': pet.comment_set.all(),
        'is_owner':is_owner,
        'is_liked': liked_by_user,
    }

    return render(request, 'pets/pet_detail.html', context)


# def comment_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             text=form.cleaned_data['text'],
#             pet=pet,
#         )
#         comment.save()
#
#     return redirect('pet details', pet.id)


@login_required
def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('pet details', pk)


@login_required
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    liked_by_user = pet.like_set.filter(user_id=request.user.id).first()
    if liked_by_user:
        liked_by_user.delete()
    else:
        like = Like(
        pet=pet,
            user=request.user
    )
        like.save()

    return redirect('pet details', pet.id)


@login_required
def create_pet(request):
    if request.method == 'POST':
        form = CreatePetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('list pets')
    else:
        form = CreatePetForm()

    context = {
        'form': form,
    }

    return render(request, 'pets/pet_create.html', context)


@login_required
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('list pets')
    else:
        form = EditPetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet_edit.html', context)


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')
    else:
        context = {
            'pet': pet,
        }
        return render(request, 'pets/pet_delete.html', context)
