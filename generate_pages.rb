require 'yaml'
require 'fileutils'

solutions = YAML.load_file('_data/solutions.yml')
output_dir = '_solutions'
FileUtils.mkdir_p(output_dir)

solutions.each do |sol|
  id = sol['id'].downcase
  filename = "#{output_dir}/#{id}.md"
  
  content = <<~HEREDOC
    ---
    layout: default
    title: "#{sol['name']}"
    permalink: /solutions/#{id}/
    solution_id: "#{sol['id']}"
    ---
    
    <div class="max-w-4xl mx-auto py-20 px-6">
      <div class="mb-10">
        <span class="text-emerald-600 font-bold tracking-widest uppercase text-xs">#{sol['category']}</span>
        <h1 class="text-5xl font-black text-slate-900 mt-2 mb-6">#{sol['name']}</h1>
        <p class="text-2xl text-slate-500 leading-relaxed">#{sol['pitch']}</p>
      </div>

      <div class="bg-white p-10 rounded-[2.5rem] shadow-xl border border-slate-100 mb-10">
        <h3 class="font-bold text-xl mb-6 flex items-center gap-3">
          <span class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-600 flex items-center justify-center">⚡</span>
          WhatsApp Logic Flow
        </h3>
        <div class="space-y-4">
          #{sol['logic'].split('->').map { |step| 
            "<div class='p-4 bg-slate-50 rounded-xl border-l-4 border-emerald-500 font-medium text-slate-700'>#{step.strip}</div>" 
          }.join("\n")}
        </div>
      </div>

      <a href="https://wa.me/{{ site.whatsapp_number }}?text=ID:#{sol['id']}" 
         class="inline-block bg-emerald-600 text-white font-black px-8 py-4 rounded-xl shadow-lg hover:bg-emerald-700 transition-all">
        Launch on WhatsApp →
      </a>
    </div>
  HEREDOC

  File.write(filename, content)
end

puts "✅ Generated #{solutions.length} solution pages in #{output_dir}/"
