from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/index.html")

Agriculture = {
    'title':'Agriculture', 
    'subtitle':'helping to feed the world',
    'images':['airspace/img/Agriculture/Ag1.png', 'airspace/img/Agriculture/Ag2.png','airspace/img/Agriculture/Ag3.png'],
    'videos':'https://www.youtube.com/embed/I7xeUFQbC04', 
    'header':'Our Work in: Argiculture',
    'text':"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nunc congue in dui vitae placerat. Suspendisse rutrum sed sapien sit amet placerat. 
    Donec fringilla urna nec posuere dictum. Nulla malesuada lectus nunc, sed fermentum massa gravida vitae. 
    Morbi erat elit, lacinia tristique libero a, feugiat ultricies dui. Integer euismod nisl risus, et dapibus diam tempus nec.
    Sed volutpat nisi id felis ultricies, a pretium purus interdum. Donec enim urna, finibus imperdiet iaculis ut, sagittis sit amet lectus. 
    Donec egestas tellus ut interdum fermentum. Curabitur at erat finibus, luctus nisl nec, ultricies lectus. 
    Integer non odio at dolor eleifend commodo. Nunc dictum nisl vitae felis mattis, ac mollis elit pharetra. Quisque in justo enim. 
    In fringilla ipsum augue, quis imperdiet tortor scelerisque eget. Etiam sed tincidunt leo. Nulla sit amet hendrerit purus, nec tempor quam. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Etiam ac ligula sodales, dictum mauris sed, volutpat sem. Quisque congue aliquet lorem, sed hendrerit eros rutrum at. 
    Donec consequat blandit dui, mattis tempor risus placerat sit amet. Phasellus vitae nibh suscipit, pulvinar arcu quis, volutpat eros. 
    Morbi condimentum sodales rhoncus. In molestie orci nulla, eget mollis felis porta ut."""
}

Architecture = {
    'title':'Architecture', 
    'subtitle':'everyone deserves a roof overhead',
    'images':['airspace/img/Building/construction1.png','airspace/img/Building/construction2.png','airspace/img/Building/construction3.png'],
    'videos':'https://www.youtube.com/embed/iQsnObyii4Q', 
    'header':'Our Work in: Architecture',
    'text':"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nunc congue in dui vitae placerat. Suspendisse rutrum sed sapien sit amet placerat. 
    Donec fringilla urna nec posuere dictum. Nulla malesuada lectus nunc, sed fermentum massa gravida vitae. 
    Morbi erat elit, lacinia tristique libero a, feugiat ultricies dui. Integer euismod nisl risus, et dapibus diam tempus nec.
    Sed volutpat nisi id felis ultricies, a pretium purus interdum. Donec enim urna, finibus imperdiet iaculis ut, sagittis sit amet lectus. 
    Donec egestas tellus ut interdum fermentum. Curabitur at erat finibus, luctus nisl nec, ultricies lectus. 
    Integer non odio at dolor eleifend commodo. Nunc dictum nisl vitae felis mattis, ac mollis elit pharetra. Quisque in justo enim. 
    In fringilla ipsum augue, quis imperdiet tortor scelerisque eget. Etiam sed tincidunt leo. Nulla sit amet hendrerit purus, nec tempor quam. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Etiam ac ligula sodales, dictum mauris sed, volutpat sem. Quisque congue aliquet lorem, sed hendrerit eros rutrum at. 
    Donec consequat blandit dui, mattis tempor risus placerat sit amet. Phasellus vitae nibh suscipit, pulvinar arcu quis, volutpat eros. 
    Morbi condimentum sodales rhoncus. In molestie orci nulla, eget mollis felis porta ut."""
    
}

Energy = {
    'title':'Energy', 
    'subtitle':'bringing power to places that have never been powered before',
    'images':['airspace/img/energy/energy1.png','airspace/img/energy/energy2.png','airspace/img/energy/energy3.png'],
    'videos':'https://www.youtube.com/embed/YzHkc9s91mk', 
    'header':'Our Work in: Energy',
    'text':"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nunc congue in dui vitae placerat. Suspendisse rutrum sed sapien sit amet placerat. 
    Donec fringilla urna nec posuere dictum. Nulla malesuada lectus nunc, sed fermentum massa gravida vitae. 
    Morbi erat elit, lacinia tristique libero a, feugiat ultricies dui. Integer euismod nisl risus, et dapibus diam tempus nec.
    Sed volutpat nisi id felis ultricies, a pretium purus interdum. Donec enim urna, finibus imperdiet iaculis ut, sagittis sit amet lectus. 
    Donec egestas tellus ut interdum fermentum. Curabitur at erat finibus, luctus nisl nec, ultricies lectus. 
    Integer non odio at dolor eleifend commodo. Nunc dictum nisl vitae felis mattis, ac mollis elit pharetra. Quisque in justo enim. 
    In fringilla ipsum augue, quis imperdiet tortor scelerisque eget. Etiam sed tincidunt leo. Nulla sit amet hendrerit purus, nec tempor quam. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Etiam ac ligula sodales, dictum mauris sed, volutpat sem. Quisque congue aliquet lorem, sed hendrerit eros rutrum at. 
    Donec consequat blandit dui, mattis tempor risus placerat sit amet. Phasellus vitae nibh suscipit, pulvinar arcu quis, volutpat eros. 
    Morbi condimentum sodales rhoncus. In molestie orci nulla, eget mollis felis porta ut."""
}

Water = {
    'title':'Water', 
    'subtitle':'Helping to make clean water a commoditiy not a privelege',
    'images':['airspace/img/Water/water1.png','airspace/img/Water/water2.png', 'airspace/img/Water/water3.png'],
    'videos':'https://www.youtube.com/embed/bx-CvvV-ofY', 
    'header':'Our Work in: Argiculture',
    'text':"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nunc congue in dui vitae placerat. Suspendisse rutrum sed sapien sit amet placerat. 
    Donec fringilla urna nec posuere dictum. Nulla malesuada lectus nunc, sed fermentum massa gravida vitae. 
    Morbi erat elit, lacinia tristique libero a, feugiat ultricies dui. Integer euismod nisl risus, et dapibus diam tempus nec.
    Sed volutpat nisi id felis ultricies, a pretium purus interdum. Donec enim urna, finibus imperdiet iaculis ut, sagittis sit amet lectus. 
    Donec egestas tellus ut interdum fermentum. Curabitur at erat finibus, luctus nisl nec, ultricies lectus. 
    Integer non odio at dolor eleifend commodo. Nunc dictum nisl vitae felis mattis, ac mollis elit pharetra. Quisque in justo enim. 
    In fringilla ipsum augue, quis imperdiet tortor scelerisque eget. Etiam sed tincidunt leo. Nulla sit amet hendrerit purus, nec tempor quam. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Etiam ac ligula sodales, dictum mauris sed, volutpat sem. Quisque congue aliquet lorem, sed hendrerit eros rutrum at. 
    Donec consequat blandit dui, mattis tempor risus placerat sit amet. Phasellus vitae nibh suscipit, pulvinar arcu quis, volutpat eros. 
    Morbi condimentum sodales rhoncus. In molestie orci nulla, eget mollis felis porta ut."""
}

PublicHealth = {'title':'PublicHealth', 
    'subtitle':'Helping people everywhere live healthy and Holistic lifes',
    'images':['airspace/img/publichealth/publicHealth1.png','airspace/img/publichealth/publicHealth2.png','airspace/img/publichealth/publicHealth3.png'],
    'videos':'https://www.youtube.com/embed/vRK7KKQH9Ck', 
    'header':'Our Work in: Argiculture',
    'text':"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nunc congue in dui vitae placerat. Suspendisse rutrum sed sapien sit amet placerat. 
    Donec fringilla urna nec posuere dictum. Nulla malesuada lectus nunc, sed fermentum massa gravida vitae. 
    Morbi erat elit, lacinia tristique libero a, feugiat ultricies dui. Integer euismod nisl risus, et dapibus diam tempus nec.
    Sed volutpat nisi id felis ultricies, a pretium purus interdum. Donec enim urna, finibus imperdiet iaculis ut, sagittis sit amet lectus. 
    Donec egestas tellus ut interdum fermentum. Curabitur at erat finibus, luctus nisl nec, ultricies lectus. 
    Integer non odio at dolor eleifend commodo. Nunc dictum nisl vitae felis mattis, ac mollis elit pharetra. Quisque in justo enim. 
    In fringilla ipsum augue, quis imperdiet tortor scelerisque eget. Etiam sed tincidunt leo. Nulla sit amet hendrerit purus, nec tempor quam. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Etiam ac ligula sodales, dictum mauris sed, volutpat sem. Quisque congue aliquet lorem, sed hendrerit eros rutrum at. 
    Donec consequat blandit dui, mattis tempor risus placerat sit amet. Phasellus vitae nibh suscipit, pulvinar arcu quis, volutpat eros. 
    Morbi condimentum sodales rhoncus. In molestie orci nulla, eget mollis felis porta ut."""
}

projects = [Agriculture,Architecture, Energy, Water, PublicHealth]

def project(request, uid=-1):
    uid = int(uid)
    page = projects[uid]
    ret = {
        'title': page['title'],
        'subtitle': page['subtitle'],
        'videos': page['videos'], 
        'images': page['images'],
        'text':page['text'],
        'header':page['header']
        
    }
    return render(request,"home/project.html", ret)