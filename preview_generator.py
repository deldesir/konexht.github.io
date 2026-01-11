import yaml
import json
import os

def generate_preview():
    # Load data
    with open('_data/solutions.yml', 'r') as f:
        solutions = yaml.safe_load(f)
    with open('_data/i18n.yml', 'r') as f:
        i18n = yaml.safe_load(f)

    # ... (rest of code)

    # Ensure output directories exist
    os.makedirs('_site', exist_ok=True)
    os.makedirs('_site/factory', exist_ok=True)

    with open('_site/index.html', 'w') as f:
        f.write(base_html.replace('{{ CONTENT }}', landing_content))
    with open('_site/factory/index.html', 'w') as f:
        f.write(base_html.replace('{{ CONTENT }}', factory_content))
    print("Preview generated at _site/index.html and _site/factory/index.html")
    nav_html = """
    <nav class="bg-white border-b border-gray-100 sticky top-0 z-50 py-4">
        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <div class="flex justify-between items-center">
                <div class="flex items-center gap-4">
                    <img src="https://raw.githubusercontent.com/deldesir/konexht.github.io/main/assets/konexlogo.png" alt="Konex Logo" class="h-10 w-auto">
                    <div class="hidden sm:block">
                        <h1 class="text-xl font-black text-slate-900 tracking-tight leading-none" x-text="t.title"></h1>
                        <p class="text-slate-400 text-[10px] font-black uppercase tracking-[0.3em] mt-1" x-text="t.subtitle"></p>
                    </div>
                </div>
                <div class="flex items-center gap-6">
                    <a href="index.html" class="text-sm font-black text-slate-400 hover:text-emerald-600 transition-all uppercase tracking-widest">Home</a>
                    <a href="index.html#services" class="text-sm font-black text-slate-400 hover:text-emerald-600 transition-all uppercase tracking-widest">Services</a>
                    <a href="factory.html" class="px-6 py-2.5 bg-emerald-600 text-white text-[10px] font-black rounded-xl uppercase tracking-widest shadow-lg shadow-emerald-200 hover:bg-emerald-700 transition-all">Solution Factory</a>
                    <div class="flex bg-slate-100 p-1 rounded-2xl border border-slate-200">
                      <button @click="lang = 'en'" :class="lang === 'en' ? 'bg-white text-emerald-600 shadow-sm' : 'text-slate-400'" class="px-3 py-1.5 rounded-xl text-[10px] font-black transition-all">EN</button>
                      <button @click="lang = 'kr'" :class="lang === 'kr' ? 'bg-white text-emerald-600 shadow-sm' : 'text-slate-400'" class="px-3 py-1.5 rounded-xl text-[10px] font-black transition-all">KR</button>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    """

    # --- Landing Page (index.html) ---
    landing_content = """
    <section class="relative py-24 overflow-hidden bg-white">
        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <div class="flex-1 text-center lg:text-left">
                    <h1 class="text-6xl font-black text-slate-900 leading-tight tracking-tighter mb-8 sm:text-7xl">
                        <span x-text="t.hero_title"></span> <br>
                        <span class="text-emerald-600" x-text="t.hero_subtitle"></span>
                    </h1>
                    <p class="text-xl text-slate-500 font-medium mb-12 max-w-2xl mx-auto lg:mx-0" x-text="t.hero_desc"></p>
                    <div class="flex flex-wrap justify-center lg:justify-start gap-6">
                        <a href="#services" class="px-10 py-5 bg-emerald-600 text-white font-black rounded-2xl shadow-xl shadow-emerald-200 hover:bg-emerald-700 transition-all uppercase tracking-widest text-xs" x-text="t.cta_services"></a>
                        <a href="factory.html" class="px-10 py-5 bg-slate-900 text-white font-black rounded-2xl shadow-xl shadow-slate-200 hover:bg-slate-800 transition-all uppercase tracking-widest text-xs" x-text="t.cta_factory"></a>
                    </div>
                </div>
                <div class="flex-1 relative">
                    <div class="absolute -inset-4 bg-emerald-100/50 rounded-[3rem] blur-2xl"></div>
                    <img src="https://raw.githubusercontent.com/deldesir/konexht.github.io/main/assets/headerimage.png" alt="KonexHT Digital Solutions" class="relative rounded-[3rem] shadow-2xl border border-slate-100">
                </div>
            </div>
        </div>
    </section>

    <section id="services" class="py-24 bg-slate-50">
        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-4xl font-black text-slate-900 tracking-tight mb-4" x-text="t.services_title"></h2>
                <p class="text-slate-400 font-medium" x-text="t.services_desc"></p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <div class="bg-white p-8 rounded-[2.5rem] border border-slate-100 shadow-sm hover:shadow-xl transition-all h-full flex flex-col">
                    <div class="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center mb-6"><svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg></div>
                    <h3 class="text-xl font-bold text-slate-900 mb-4" x-text="t.service_writing"></h3>
                    <p class="text-slate-500 text-sm font-medium mb-8 flex-grow" x-text="t.service_writing_desc"></p>
                    <button class="text-blue-600 text-xs font-black uppercase tracking-widest hover:underline" x-text="t.overview"></button>
                </div>
                <div class="bg-white p-8 rounded-[2.5rem] border border-slate-100 shadow-sm hover:shadow-xl transition-all h-full flex flex-col">
                    <div class="w-14 h-14 bg-purple-50 text-purple-600 rounded-2xl flex items-center justify-center mb-6"><svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg></div>
                    <h3 class="text-xl font-bold text-slate-900 mb-4" x-text="t.service_design"></h3>
                    <p class="text-slate-500 text-sm font-medium mb-8 flex-grow" x-text="t.service_design_desc"></p>
                    <button class="text-purple-600 text-xs font-black uppercase tracking-widest hover:underline" x-text="t.overview"></button>
                </div>
                <div class="bg-white p-8 rounded-[2.5rem] border border-slate-100 shadow-sm hover:shadow-xl transition-all h-full flex flex-col">
                    <div class="w-14 h-14 bg-amber-50 text-amber-600 rounded-2xl flex items-center justify-center mb-6"><svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg></div>
                    <h3 class="text-xl font-bold text-slate-900 mb-4" x-text="t.service_literacy"></h3>
                    <p class="text-slate-500 text-sm font-medium mb-8 flex-grow" x-text="t.service_literacy_desc"></p>
                    <button class="text-amber-600 text-xs font-black uppercase tracking-widest hover:underline" x-text="t.overview"></button>
                </div>
                <div class="bg-emerald-900 p-8 rounded-[2.5rem] border border-emerald-800 shadow-2xl hover:scale-105 transition-all h-full flex flex-col ring-8 ring-emerald-500/10">
                    <div class="w-14 h-14 bg-white/10 text-emerald-400 rounded-2xl flex items-center justify-center mb-6"><svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg></div>
                    <h3 class="text-xl font-bold text-white mb-4" x-text="t.service_factory"></h3>
                    <p class="text-emerald-100/70 text-sm font-medium mb-8 flex-grow" x-text="t.service_factory_desc"></p>
                    <a href="factory.html" class="text-emerald-400 text-xs font-black uppercase tracking-widest hover:text-white inline-flex items-center gap-2">
                        <span x-text="t.blueprint"></span> <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>
    """

    # --- Factory Page (factory.html) ---
    factory_content = """
    <div x-data="{ search: '', category: 'All' }">
        <section class="mb-16 -mt-8">
            <div class="bg-emerald-900 -mx-6 lg:-mx-8 py-4 mb-16 overflow-hidden">
                <div class="max-w-7xl mx-auto px-6 flex flex-wrap gap-10 justify-center md:justify-start">
                    <div class="flex items-center gap-3"><span class="text-2xl font-black text-white" x-text="solutions.length"></span><span class="text-[10px] font-black text-emerald-300 uppercase tracking-widest">Solutions</span></div>
                    <div class="flex items-center gap-3 border-l border-white/10 pl-10"><span class="text-2xl font-black text-emerald-400">100%</span><span class="text-[10px] font-black text-slate-300 uppercase tracking-widest">WhatsApp Linear</span></div>
                    <div class="flex items-center gap-3 border-l border-white/10 pl-10"><span class="text-2xl font-black text-amber-400">5/5</span><span class="text-[10px] font-black text-slate-300 uppercase tracking-widest">Lead Impact</span></div>
                </div>
            </div>
            <div class="text-center mb-16">
                <h1 class="text-6xl font-black tracking-tighter text-slate-900 sm:text-7xl mb-4"><span x-text="t.title"></span> <span class="text-emerald-600" x-text="t.subtitle"></span></h1>
                <p class="text-xl text-slate-400 max-w-2xl mx-auto font-medium" x-text="t.search_placeholder"></p>
            </div>
            <div class="flex flex-col md:flex-row gap-4 mb-12">
                <div class="relative flex-grow">
                    <span class="absolute inset-y-0 left-0 pl-8 flex items-center text-slate-300"><svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg></span>
                    <input type="text" x-model="search" :placeholder="t.search_placeholder" class="block w-full pl-20 pr-8 py-6 border-2 border-slate-100 rounded-[2.5rem] focus:ring-emerald-500 focus:border-emerald-500 text-xl font-bold shadow-sm bg-white transition-all outline-none">
                </div>
                <div class="md:w-72 relative">
                    <select x-model="category" class="block w-full py-6 px-10 border-2 border-slate-100 bg-white rounded-[2.5rem] focus:ring-emerald-500 focus:border-emerald-500 text-lg font-bold text-slate-600 appearance-none shadow-sm cursor-pointer outline-none">
                        <option value="All">All Categories</option>
                        <template x-for="cat in [...new Set(solutions.map(s => s.category))]"><option :value="cat" x-text="cat"></option></template>
                    </select>
                </div>
            </div>
        </section>
        <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            <template x-for="solution in solutions">
                <div @click="activeSolution = solution; showModal = true; modalTab = 'overview'" class="group relative bg-white rounded-[2.5rem] border-2 border-slate-50 p-8 shadow-sm transition-all hover:shadow-2xl hover:-translate-y-2 hover:border-emerald-100 flex flex-col cursor-pointer" x-show="(category === 'All' || category === solution.category) && (solution.name + solution.id + solution.pitch).toLowerCase().includes(search.toLowerCase())">
                    <button @click.stop="toggleFav(solution)" class="absolute top-6 right-6 z-20 p-3 rounded-2xl transition-all" :class="favorites.find(f => f.id === solution.id) ? 'bg-emerald-600 text-white shadow-lg' : 'bg-slate-50 text-slate-300 hover:text-emerald-600'"><svg class="h-5 w-5" :fill="favorites.find(f => f.id === solution.id) ? 'currentColor' : 'none'" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.382-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path></svg></button>
                    <div class="mb-4"><span class="px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest bg-emerald-50 text-emerald-600" x-text="solution.category"></span></div>
                    <div class="flex-grow"><h3 class="text-xl font-bold text-slate-900 mb-2 truncate group-hover:text-emerald-600 transition-colors tracking-tight" x-text="solution.name"></h3><p class="text-slate-400 text-sm font-medium line-clamp-3 mb-6" x-text="solution.pitch"></p></div>
                    <div class="pt-6 border-t border-slate-50 flex items-center justify-between"><span class="text-emerald-600 text-xs font-black uppercase tracking-widest underline decoration-2 underline-offset-4">Blueprint</span><div class="flex items-center gap-1.5"><span class="text-[10px] font-black text-slate-300 uppercase">ROI</span><span class="text-xs font-black text-emerald-600" x-text="solution.metrics.roi"></span></div></div>
                </div>
            </template>
        </div>
    </div>
    """

    base_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>KonexHT - Local Preview</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        [x-cloak] { display: none !important; }
        @keyframes slideInRight { from { transform: translateX(20px); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        .animate-bubble { animation: slideInRight 0.4s ease-out forwards; }
    </style>
    <script>
        window.SOLUTIONS_DATA = """ + json.dumps(solutions) + """;
        window.I18N_DATA = """ + json.dumps(i18n) + """;
        tailwind.config = { theme: { extend: { colors: { emerald: { 600: '#059669', 900: '#064e3b' } } } } }
    </script>
</head>
<body class="bg-gray-50 text-gray-900" x-data="{ lang: 'kr', solutions: SOLUTIONS_DATA, i18n: window.I18N_DATA, activeSolution: null, showModal: false, modalTab: 'overview', favorites: JSON.parse(localStorage.getItem('konexht_favs') || '[]'), get t() { return this.i18n[this.lang]; } }">
    """ + nav_html + """
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {{ CONTENT }}
    </main>
    <footer class="bg-white border-t border-gray-100 py-12 mt-24 text-center">
        <p class="text-slate-400 text-sm">© 2026 KonexHT Digital Solutions. Empowering Impact.</p>
    </footer>
</body>
</html>
"""

    with open('/tmp/index.html', 'w') as f:
        f.write(base_html.replace('{{ CONTENT }}', landing_content))
    with open('/tmp/factory.html', 'w') as f:
        f.write(base_html.replace('{{ CONTENT }}', factory_content))
    print("Preview generated at /tmp/index.html and /tmp/factory.html")

if __name__ == "__main__":
    generate_preview()
