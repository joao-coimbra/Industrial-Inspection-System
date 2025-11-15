#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Industrial Inspection System - Part Management, Quality and Storage
Author: João Henrique Benatti Coimbra
Institution: UniFECAF
Course: Algorithms and Programming Logic
Date: 15/11/2025

Description:
    Digital automation prototype for inspection, classification and storage
    of industrial parts based on pre-defined quality criteria.
    
Concepts used:
    - Variables and basic data types
    - Conditional structures (if/elif/else)
    - Loop structures (while/for)
    - Lists and dictionaries
    - Simple functions for modularization
"""

# ============================================================================
# SYSTEM CONSTANTS - Quality Criteria
# ============================================================================

MIN_WEIGHT = 95
MAX_WEIGHT = 105
VALID_COLORS = ["azul", "verde"]
MIN_LENGTH = 10
MAX_LENGTH = 20
BOX_CAPACITY = 10

# ============================================================================
# GLOBAL DATA STRUCTURES
# ============================================================================

approved_parts = []
rejected_parts = []
closed_boxes = []
current_box = []
id_counter = 0


# ============================================================================
# QUALITY VALIDATION FUNCTION
# ============================================================================

def validate_part(weight, color, length):
    """
    Validates part parameters according to established quality criteria.
    
    Parameters:
        weight (float): Part weight in grams
        color (str): Part color (azul or verde)
        length (float): Part length in centimeters
    
    Returns:
        tuple: (boolean indicating approval, string with rejection reason)
    """
    
    # Weight validation
    if weight < MIN_WEIGHT or weight > MAX_WEIGHT:
        return False, f"Peso fora do intervalo [{MIN_WEIGHT}g-{MAX_WEIGHT}g]"
    
    # Color validation
    if color not in VALID_COLORS:
        return False, "Cor não conforme [azul/verde]"
    
    # Length validation
    if length < MIN_LENGTH or length > MAX_LENGTH:
        return False, f"Comprimento fora do intervalo [{MIN_LENGTH}cm-{MAX_LENGTH}cm]"
    
    # Part approved in all criteria
    return True, ""


# ============================================================================
# PART REGISTRATION FUNCTION
# ============================================================================

def register_part():
    """
    Registers a new part in the system through interactive input.
    Performs quality validation and stores in appropriate structures.
    """
    global id_counter, approved_parts, rejected_parts, current_box, closed_boxes
    
    print("\n" + "="*60)
    print("           CADASTRO DE NOVA PEÇA")
    print("="*60)
    
    # Unique identifier increment
    id_counter = id_counter + 1
    print(f"ID gerado automaticamente: {id_counter}")
    
    # Part data collection with error handling
    try:
        weight = float(input("Digite o peso (g): "))
        color = input("Digite a cor (azul/verde): ").lower().strip()
        length = float(input("Digite o comprimento (cm): "))
    except ValueError:
        print("✗ ERRO: Entrada inválida. Peso e comprimento devem ser números.")
        id_counter = id_counter - 1  # Reverts ID increment
        return
    
    # Part validation
    is_approved, reason = validate_part(weight, color, length)
    
    if is_approved:
        # Creating approved part record
        part = {
            "id": id_counter,
            "weight": weight,
            "color": color,
            "length": length
        }
        
        # Storage in data structures
        approved_parts.append(part)
        current_box.append(part)
        
        print(f"\n✓ PEÇA APROVADA - ID: {id_counter}")
        print(f"  Peso: {weight}g | Cor: {color} | Comprimento: {length}cm")
        
        # Box closure verification
        if len(current_box) == BOX_CAPACITY:
            closed_boxes.append(current_box.copy())
            box_number = len(closed_boxes)
            print(f"\n✓✓ CAIXA {box_number} FECHADA - {BOX_CAPACITY} peças armazenadas")
            current_box.clear()
    else:
        # Creating rejected part record
        rejected_part = {
            "id": id_counter,
            "weight": weight,
            "color": color,
            "length": length,
            "reason": reason
        }
        
        rejected_parts.append(rejected_part)
        print(f"\n✗ PEÇA REPROVADA - ID: {id_counter}")
        print(f"  Motivo: {reason}")


# ============================================================================
# PARTS LISTING FUNCTION
# ============================================================================

def list_parts():
    """
    Displays complete listing of all approved and rejected parts registered.
    """
    print("\n" + "="*60)
    print("           PEÇAS APROVADAS")
    print("="*60)
    
    if len(approved_parts) == 0:
        print("  Nenhuma peça aprovada cadastrada.")
    else:
        print(f"  Total: {len(approved_parts)} peça(s)\n")
        for part in approved_parts:
            print(f"  ID: {part['id']:03d} | Peso: {part['weight']:6.2f}g | "
                  f"Cor: {part['color']:6s} | Comprimento: {part['length']:5.2f}cm")
    
    print("\n" + "="*60)
    print("           PEÇAS REPROVADAS")
    print("="*60)
    
    if len(rejected_parts) == 0:
        print("  Nenhuma peça reprovada cadastrada.")
    else:
        print(f"  Total: {len(rejected_parts)} peça(s)\n")
        for part in rejected_parts:
            print(f"  ID: {part['id']:03d} | Motivo: {part['reason']}")


# ============================================================================
# PART REMOVAL FUNCTION
# ============================================================================

def remove_part():
    """
    Removes a part from the system through the informed ID.
    Searches all data structures and removes the first occurrence.
    """
    global approved_parts, rejected_parts, current_box, closed_boxes
    
    print("\n" + "="*60)
    print("           REMOÇÃO DE PEÇA")
    print("="*60)
    
    try:
        id_to_remove = int(input("Digite o ID da peça a remover: "))
    except ValueError:
        print("✗ ERRO: ID inválido. Digite um número inteiro.")
        return
    
    found = False
    
    # Search in approved parts
    for index in range(len(approved_parts)):
        if approved_parts[index]["id"] == id_to_remove:
            approved_parts.pop(index)
            found = True
            
            # Remove from current box if present
            for i in range(len(current_box)):
                if current_box[i]["id"] == id_to_remove:
                    current_box.pop(i)
                    break
            
            # Remove from closed boxes if present
            for box in closed_boxes:
                for i in range(len(box)):
                    if box[i]["id"] == id_to_remove:
                        box.pop(i)
                        break
            
            break
    
    # If not found in approved, search in rejected
    if not found:
        for index in range(len(rejected_parts)):
            if rejected_parts[index]["id"] == id_to_remove:
                rejected_parts.pop(index)
                found = True
                break
    
    # User feedback
    if found:
        print(f"\n✓ Peça ID {id_to_remove} removida com sucesso do sistema.")
    else:
        print(f"\n✗ Peça ID {id_to_remove} não encontrada no sistema.")


# ============================================================================
# BOXES LISTING FUNCTION
# ============================================================================

def list_boxes():
    """
    Displays all closed boxes and the current box with their parts.
    """
    print("\n" + "="*60)
    print("           CAIXAS DE ARMAZENAMENTO")
    print("="*60)
    
    if len(closed_boxes) == 0 and len(current_box) == 0:
        print("  Nenhuma caixa registrada no sistema.")
        return
    
    # Closed boxes listing
    if len(closed_boxes) > 0:
        print(f"\n  CAIXAS FECHADAS: {len(closed_boxes)}\n")
        for index in range(len(closed_boxes)):
            box = closed_boxes[index]
            print(f"  ╔═══ CAIXA {index + 1:02d} ═══╗")
            print(f"  ║ Status: FECHADA | Peças: {len(box)}/{BOX_CAPACITY}")
            print(f"  ╚{'═'*17}╝")
            
            for part in box:
                print(f"    - ID: {part['id']:03d} | Peso: {part['weight']:6.2f}g | "
                      f"Cor: {part['color']:6s}")
            print()
    
    # Current box listing
    if len(current_box) > 0:
        print("  ╔═══ CAIXA EM ANDAMENTO ═══╗")
        print(f"  ║ Status: ABERTA | Peças: {len(current_box)}/{BOX_CAPACITY}")
        print(f"  ╚{'═'*25}╝")
        
        for part in current_box:
            print(f"    - ID: {part['id']:03d} | Peso: {part['weight']:6.2f}g | "
                  f"Cor: {part['color']:6s}")


# ============================================================================
# REPORT GENERATION FUNCTION
# ============================================================================

def generate_report():
    """
    Generates consolidated report with production and quality indicators.
    Presents metrics, approval analysis and rejection detailing.
    """
    print("\n" + "="*60)
    print("      RELATÓRIO CONSOLIDADO DE PRODUÇÃO")
    print("="*60)
    
    # Metrics calculation
    total_approved = len(approved_parts)
    total_rejected = len(rejected_parts)
    total_parts = total_approved + total_rejected
    total_closed_boxes = len(closed_boxes)
    parts_in_current_box = len(current_box)
    
    # Approval rate calculation
    if total_parts > 0:
        approval_rate = (total_approved / total_parts) * 100
    else:
        approval_rate = 0.0
    
    # Report display
    print("\n📊 INDICADORES GERAIS:")
    print(f"  • Total de peças processadas: {total_parts}")
    print(f"  • Peças aprovadas: {total_approved}")
    print(f"  • Peças reprovadas: {total_rejected}")
    print(f"  • Taxa de aprovação: {approval_rate:.2f}%")
    
    print("\n📦 ARMAZENAMENTO:")
    print(f"  • Caixas fechadas: {total_closed_boxes}")
    print(f"  • Peças na caixa atual: {parts_in_current_box}/{BOX_CAPACITY}")
    
    # Rejections detailing
    print("\n" + "-"*60)
    if total_rejected > 0:
        print("❌ DETALHAMENTO DE REPROVAÇÕES:")
        print()
        
        # Reasons counting
        reasons = {}
        for part in rejected_parts:
            reason = part["reason"]
            if reason in reasons:
                reasons[reason] = reasons[reason] + 1
            else:
                reasons[reason] = 1
        
        print("  Reprovações por motivo:")
        for reason, quantity in reasons.items():
            percentage = (quantity / total_rejected) * 100
            print(f"    • {reason}: {quantity} ({percentage:.1f}%)")
        
        print("\n  Lista completa de peças reprovadas:")
        for part in rejected_parts:
            print(f"    • ID {part['id']:03d}: {part['reason']}")
    else:
        print("✓ Nenhuma peça reprovada registrada.")
    
    print("="*60)


# ============================================================================
# AUTO-FILL FUNCTION (DEMONSTRATION)
# ============================================================================

def auto_fill():
    """
    Automatically registers a set of parts for system demonstration.
    Includes approved and rejected parts by different reasons to exemplify
    all functionalities during presentations and pitch videos.
    """
    global id_counter, approved_parts, rejected_parts, current_box, closed_boxes
    
    print("\n" + "="*60)
    print("      PREENCHIMENTO AUTOMÁTICO - MODO DEMONSTRAÇÃO")
    print("="*60)
    print("\nCadastrando peças de exemplo...\n")
    
    # Demonstration database
    # Format: (weight, color, length)
    demo_parts = [
        # APPROVED parts (first 10 to close first box)
        (100.0, "azul", 15.0),      # ID 1
        (98.5, "verde", 12.5),      # ID 2
        (102.0, "azul", 18.0),      # ID 3
        (96.0, "verde", 14.0),      # ID 4
        (104.0, "azul", 16.5),      # ID 5
        (99.0, "verde", 11.0),      # ID 6
        (101.5, "azul", 19.0),      # ID 7
        (97.0, "verde", 13.5),      # ID 8
        (103.0, "azul", 17.0),      # ID 9
        (100.5, "verde", 15.5),     # ID 10 - CLOSES BOX 1
        
        # More APPROVED parts (for current box)
        (98.0, "azul", 12.0),       # ID 11
        (102.5, "verde", 14.5),     # ID 12
        (99.5, "azul", 16.0),       # ID 13
        
        # REJECTED parts by WEIGHT
        (90.0, "azul", 15.0),       # ID 14 - Weight below
        (110.0, "verde", 12.0),     # ID 15 - Weight above
        
        # REJECTED parts by COLOR
        (100.0, "vermelho", 15.0),  # ID 16 - Invalid color
        (98.0, "amarelo", 14.0),    # ID 17 - Invalid color
        
        # REJECTED parts by LENGTH
        (100.0, "azul", 8.0),       # ID 18 - Length below
        (99.0, "verde", 25.0),      # ID 19 - Length above
        
        # More APPROVED parts
        (95.0, "verde", 10.0),      # ID 20 - Minimum limit
        (105.0, "azul", 20.0),      # ID 21 - Maximum limit
    ]
    
    # Processing demonstration parts
    for weight, color, length in demo_parts:
        id_counter = id_counter + 1
        
        # Part validation
        is_approved, reason = validate_part(weight, color, length)
        
        if is_approved:
            part = {
                "id": id_counter,
                "weight": weight,
                "color": color,
                "length": length
            }
            
            approved_parts.append(part)
            current_box.append(part)
            
            print(f"✓ ID {id_counter:03d}: APROVADA | {weight}g | {color} | {length}cm")
            
            # Box closure verification
            if len(current_box) == BOX_CAPACITY:
                closed_boxes.append(current_box.copy())
                print(f"  >> CAIXA {len(closed_boxes)} FECHADA!")
                current_box.clear()
        else:
            rejected_part = {
                "id": id_counter,
                "weight": weight,
                "color": color,
                "length": length,
                "reason": reason
            }
            
            rejected_parts.append(rejected_part)
            print(f"✗ ID {id_counter:03d}: REPROVADA | {reason}")
    
    print(f"\n{'='*60}")
    print("✓ Preenchimento automático concluído!")
    print(f"  • {len(approved_parts)} peças aprovadas cadastradas")
    print(f"  • {len(rejected_parts)} peças reprovadas cadastradas")
    print(f"  • {len(closed_boxes)} caixa(s) fechada(s)")
    print(f"  • {len(current_box)} peça(s) na caixa em andamento")
    print(f"{'='*60}")


# ============================================================================
# MENU DISPLAY FUNCTION
# ============================================================================

def display_menu():
    """
    Displays system main menu with all available options.
    """
    print("\n" + "╔" + "="*58 + "╗")
    print("║  SISTEMA DE INSPEÇÃO INDUSTRIAL - v1.0" + " "*19 + "║")
    print("║  Gestão de Peças, Qualidade e Armazenamento" + " "*14 + "║")
    print("╚" + "="*58 + "╝")
    print("\n  [1] Cadastrar nova peça")
    print("  [2] Listar peças aprovadas/reprovadas")
    print("  [3] Remover peça cadastrada")
    print("  [4] Listar caixas fechadas")
    print("  [5] Gerar relatório final")
    print("  [6] Preenchimento automático (DEMO)")
    print("  [0] Sair do sistema")
    print("  " + "─"*56)


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """
    Main function that initializes and executes the system loop.
    """
    print("\n" + "="*60)
    print("  INICIALIZANDO SISTEMA DE INSPEÇÃO INDUSTRIAL")
    print("="*60)
    print("\n  Sistema pronto para uso.")
    print("  Critérios de qualidade:")
    print(f"    • Peso: {MIN_WEIGHT}g - {MAX_WEIGHT}g")
    print(f"    • Cor: {', '.join(VALID_COLORS)}")
    print(f"    • Comprimento: {MIN_LENGTH}cm - {MAX_LENGTH}cm")
    
    # System main loop
    while True:
        display_menu()
        option = input("\n  Escolha uma opção: ").strip()
        
        if option == "1":
            register_part()
        elif option == "2":
            list_parts()
        elif option == "3":
            remove_part()
        elif option == "4":
            list_boxes()
        elif option == "5":
            generate_report()
        elif option == "6":
            auto_fill()
        elif option == "0":
            print("\n" + "="*60)
            print("  Encerrando sistema...")
            print("  Obrigado por utilizar o Sistema de Inspeção Industrial.")
            print("="*60 + "\n")
            break
        else:
            print("\n✗ Opção inválida. Por favor, escolha uma opção válida.")
        
        # Pause for visualization
        input("\nPressione ENTER para continuar...")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
